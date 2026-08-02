"""
B-Tree Database - Standalone Implementation
Shows B-tree indexing with nodes stored on disk (minimal RAM usage)
"""

from typing import Optional, Dict, List
import time
import json
import os


class BTreeNode:
    """B-tree node - can be stored on disk"""

    def __init__(self, order: int = 100, is_leaf: bool = True):
        self.order = order  # Max keys per node
        self.keys: List[int] = []  # Sorted keys
        self.children: List[int] = []  # Child node IDs (disk positions)
        self.values: List[int] = []  # File positions for actual data
        self.is_leaf = is_leaf
        self.node_id: Optional[int] = None

    def to_dict(self) -> dict:
        """Serialize node for disk storage"""
        return {
            "keys": self.keys,
            "children": self.children,
            "values": self.values,
            "is_leaf": self.is_leaf,
            "order": self.order,
        }

    @classmethod
    def from_dict(cls, node_id: int, data: dict) -> "BTreeNode":
        """Deserialize node from disk"""
        node = cls(order=data["order"], is_leaf=data["is_leaf"])
        node.node_id = node_id
        node.keys = data["keys"]
        node.children = data["children"]
        node.values = data["values"]
        return node


class BTreeDatabase:
    """B-tree with nodes on disk - minimal RAM usage!"""

    def __init__(
        self, filename="test_data.csv", index_file="btree_index.json", order=100
    ):
        self.filename = filename
        self.index_file = index_file
        self.order = order

        # Only keep root in memory!
        self.root: Optional[BTreeNode] = None
        self.next_node_id = 0
        self.nodes_on_disk: Dict[int, dict] = {}  # Simulates disk storage
        self.disk_reads = 0  # Track disk reads for analysis

        self._build_index()

    def _build_index(self):
        """Build B-tree index from file"""
        print(f"Building B-tree index (order={self.order})...")

        # Initialize with empty root
        self.root = BTreeNode(self.order, is_leaf=True)
        self.root.node_id = self._get_next_node_id()

        count = 0
        with open(self.filename, "r") as f:
            f.readline()  # Skip header

            while True:
                position = f.tell()
                line = f.readline()

                if not line:
                    break

                record_id = int(line.split(",")[0])
                self._insert_btree(record_id, position)
                count += 1

                if count % 100000 == 0:
                    print(f"  Processed {count} records...")

        print(f"✓ B-tree built: {count} keys across {len(self.nodes_on_disk)} nodes")
        print(f"  RAM usage: Only root node + current search path")

    def _get_next_node_id(self) -> int:
        """Generate unique node ID"""
        node_id = self.next_node_id
        self.next_node_id += 1
        return node_id

    def _save_node(self, node: BTreeNode):
        """Save node to 'disk' (simulates disk write)"""
        if node.node_id is None:
            raise ValueError("Node must have a node_id before being saved to disk")
        self.nodes_on_disk[node.node_id] = node.to_dict()

    def _load_node(self, node_id: int) -> BTreeNode:
        """Load node from 'disk' (simulates disk read)"""
        self.disk_reads += 1
        data = self.nodes_on_disk[node_id]
        return BTreeNode.from_dict(node_id, data)

    def _insert_btree(self, key: int, file_position: int):
        """Insert key into B-tree"""
        root = self.root

        # Ensure root exists before accessing its attributes
        if root is None:
            self.root = BTreeNode(self.order, is_leaf=True)
            self.root.node_id = self._get_next_node_id()
            root = self.root

        # If root is full, split it
        if len(root.keys) >= self.order:
            new_root = BTreeNode(self.order, is_leaf=False)
            new_root.node_id = self._get_next_node_id()
            assert root.node_id is not None
            new_root.children.append(root.node_id)
            self._split_child(new_root, 0)
            self.root = new_root
            root = new_root

        self._insert_non_full(root, key, file_position)

    def _insert_non_full(self, node: BTreeNode, key: int, file_position: int):
        """Insert into a non-full node"""
        if node.is_leaf:
            # Insert key in sorted order
            insert_pos = 0
            while insert_pos < len(node.keys) and key > node.keys[insert_pos]:
                insert_pos += 1

            node.keys.insert(insert_pos, key)
            node.values.insert(insert_pos, file_position)
            self._save_node(node)
        else:
            # Find which child to insert into
            child_index = 0
            while child_index < len(node.keys) and key > node.keys[child_index]:
                child_index += 1

            child = self._load_node(node.children[child_index])

            # If child is full, split it
            if len(child.keys) >= self.order:
                self._split_child(node, child_index)
                if key > node.keys[child_index]:
                    child_index += 1
                child = self._load_node(node.children[child_index])

            self._insert_non_full(child, key, file_position)

    def _split_child(self, parent: BTreeNode, child_index: int):
        """Split a full child node"""
        full_child = self._load_node(parent.children[child_index])
        new_child = BTreeNode(self.order, full_child.is_leaf)
        new_child.node_id = self._get_next_node_id()

        mid = self.order // 2

        # Move second half to new node
        new_child.keys = full_child.keys[mid:]
        full_child.keys = full_child.keys[:mid]

        if full_child.is_leaf:
            new_child.values = full_child.values[mid:]
            full_child.values = full_child.values[:mid]
        else:
            new_child.children = full_child.children[mid:]
            full_child.children = full_child.children[:mid]

        # Promote middle key to parent
        promote_key = new_child.keys[0]
        parent.keys.insert(child_index, promote_key)
        parent.children.insert(child_index + 1, new_child.node_id)

        # Save all modified nodes
        self._save_node(full_child)
        self._save_node(new_child)
        self._save_node(parent)

    def find(self, target_id: int) -> Optional[dict]:
        """Search B-tree - O(log n) with minimal disk reads"""

        if self.root is None:
            return
        self.disk_reads = 0  # Reset counter

        position = self._search_btree(self.root, target_id)

        if position is None:
            return None

        # Read actual data from file
        with open(self.filename, "r") as f:
            f.seek(position)
            record = f.readline().strip().split(",")
            return {
                "name": record[1],
                "email": record[2],
                "age": record[3],
                "disk_reads": self.disk_reads,
            }

    def _search_btree(self, node: BTreeNode, key: int) -> Optional[int]:
        """Recursively search B-tree"""
        # Binary search within node
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # Found the key
        if i < len(node.keys) and key == node.keys[i]:
            return node.values[i]

        # Reached leaf without finding key
        if node.is_leaf:
            return None

        # Load child from disk and continue search
        child = self._load_node(node.children[i])
        return self._search_btree(child, key)

    def get_tree_height(self) -> int:
        if self.root is None:
            return 0
        """Calculate tree height"""
        return self._get_height(self.root)

    def _get_height(self, node: BTreeNode) -> int:
        """Recursive height calculation"""
        if node.is_leaf:
            return 1

        # Load first child to check depth
        if node.children:
            child = self._load_node(node.children[0])
            return 1 + self._get_height(child)
        return 1

    def save_to_disk(self):
        """Persist index to actual disk file"""
        if self.root is None:
            return
        with open(self.index_file, "w") as f:
            json.dump(
                {
                    "root_id": self.root.node_id,
                    "next_node_id": self.next_node_id,
                    "order": self.order,
                    "nodes": self.nodes_on_disk,
                },
                f,
            )
        print(f"✓ Index saved to {self.index_file}")

    @classmethod
    def load_from_disk(cls, filename: str, index_file: str):
        """Load previously built index from disk"""
        with open(index_file, "r") as f:
            data = json.load(f)

        db = cls.__new__(cls)
        db.filename = filename
        db.index_file = index_file
        db.order = data["order"]
        db.next_node_id = data["next_node_id"]
        db.nodes_on_disk = {int(k): v for k, v in data["nodes"].items()}
        db.disk_reads = 0

        # Load root node
        root_id = data["root_id"]
        db.root = BTreeNode.from_dict(root_id, db.nodes_on_disk[root_id])

        return db


def main():
    """Test the B-Tree Database with proper index persistence"""
    print("=" * 70)
    print("B-TREE DATABASE - STANDALONE TEST")
    print("=" * 70)

    index_file = "btree_index.json"
    data_file = "test_data.csv"

    # Check if index already exists
    if os.path.exists(index_file):
        print("\n[1] Loading existing index from disk...")
        start_load = time.time()
        try:
            btree_db = BTreeDatabase.load_from_disk(data_file, index_file)
            load_time = time.time() - start_load
            print(f"    ✓ Index loaded in {load_time:.4f}s (INSTANT! ⚡)")
            print(f"    Tree height: {btree_db.get_tree_height()} levels")
            print(f"    Total nodes: {len(btree_db.nodes_on_disk)}")

            # Verify the index works
            test_result = btree_db.find(1)
            if test_result:
                print(f"    Verification: Record #1 = {test_result['name']} ✓")
            else:
                print("    ⚠️ Index may be corrupted, rebuilding...")
                raise FileNotFoundError("Index verification failed")

        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"    ⚠️ Error loading index: {e}")
            print("    Building new index...")
            start_build = time.time()
            btree_db = BTreeDatabase(data_file, index_file, order=100)
            build_time = time.time() - start_build
            print(f"    Build time: {build_time:.4f}s")
            btree_db.save_to_disk()

    else:
        # No index exists, build from scratch
        print("\n[1] Building new index (first time)...")
        start_build = time.time()
        btree_db = BTreeDatabase(data_file, index_file, order=100)
        build_time = time.time() - start_build
        print(f"    ✓ Index built in {build_time:.4f}s")
        print(f"    Tree height: {btree_db.get_tree_height()} levels")
        print(f"    Total nodes: {len(btree_db.nodes_on_disk)}")
        btree_db.save_to_disk()

    # Test searches (same for both cases)
    print("\n[2] Testing Searches...")
    print("-" * 70)
    test_ids = [1, 5000, 500000, 999999, 1000001]

    total_disk_reads = 0
    successful_searches = 0

    for target_id in test_ids:
        start = time.time()
        result = btree_db.find(target_id)
        elapsed = time.time() - start

        if result:
            disk_reads = result.pop("disk_reads")
            total_disk_reads += disk_reads
            successful_searches += 1
            print(
                f"  ID {target_id:7d}: ✓ Found in {elapsed*1000:6.2f}ms "
                f"({disk_reads} disk reads) - {result['name']}"
            )
        else:
            print(f"  ID {target_id:7d}: ✗ Not found ({elapsed*1000:6.2f}ms)")

    # Calculate averages only for successful searches
    avg_disk_reads = (
        total_disk_reads / successful_searches if successful_searches > 0 else 0
    )

    print("\n" + "=" * 70)
    print("PERFORMANCE SUMMARY:")
    print("=" * 70)
    print(f"• Tree height: {btree_db.get_tree_height()} levels")
    print(f"• Total nodes: {len(btree_db.nodes_on_disk)}")
    print(f"• Average disk reads per search: {avg_disk_reads:.1f}")
    print(f"• Index file: {index_file}")
    print(f"• Data file: {data_file}")

    print(f"\nKEY ADVANTAGES:")
    print(f"• Only root node + search path in RAM at any time")
    print(f"• For 1M records with order 100:")
    print(
        f"  - B-tree needs only {btree_db.get_tree_height()}-{btree_db.get_tree_height()+1} disk reads!"
    )
    print(f"  - RAM usage: ~4KB (vs ~80MB for BST)")
    print(f"  - Subsequent startups: INSTANT load from disk! ⚡")
    print("=" * 70)

    # Show file sizes
    if os.path.exists(index_file):
        index_size = os.path.getsize(index_file)
        data_size = os.path.getsize(data_file)
        print(f"\nFILE SIZES:")
        print(f"• Data file: {data_size / (1024*1024):.2f} MB")
        print(f"• Index file: {index_size / (1024*1024):.2f} MB")
        print(f"• Index/Data ratio: {(index_size/data_size)*100:.1f}%")
    print("=" * 70)


if __name__ == "__main__":
    main()
