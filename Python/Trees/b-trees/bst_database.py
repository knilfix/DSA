"""
Binary Search Tree Database - Standalone Implementation
Shows BST indexing approach with all nodes in RAM
"""

from typing import Optional
import time


class BSTNode:
    """A single node in the binary search tree"""

    def __init__(self, key: int, file_position: int) -> None:
        self.key = key
        self.file_position = file_position
        self.left: Optional["BSTNode"] = None
        self.right: Optional["BSTNode"] = None


class BSTDatabase:
    """Binary Search Tree index - all nodes stored in RAM"""

    def __init__(self, filename="test_data.csv") -> None:
        self.filename = filename
        self.root = None
        self._build_index()

    def _build_index(self):
        """Build BST from file by reading all records"""
        print("Building BST index...")
        count = 0

        with open(self.filename, "r") as f:
            f.readline()  # Skip header

            while True:
                position = f.tell()
                line = f.readline()

                if not line:
                    break

                record = line.strip().split(",")
                record_id = int(record[0])
                self._insert_node(key=record_id, file_position=position)
                count += 1

                if count % 100000 == 0:
                    print(f"  Processed {count} records...")

        print(f"✓ BST index built with {count} records (all in RAM)")

    def _insert_node(self, key: int, file_position: int):
        """Insert into BST iteratively (avoids recursion depth issues)"""
        if self.root is None:
            self.root = BSTNode(key=key, file_position=file_position)
            return

        current = self.root
        while current:
            if key < current.key:
                if current.left is None:
                    current.left = BSTNode(key=key, file_position=file_position)
                    return
                else:
                    current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = BSTNode(key=key, file_position=file_position)
                    return
                else:
                    current = current.right
            else:
                # Key already exists - update the file position
                current.file_position = file_position
                return

    def find(self, target_id: int) -> Optional[dict]:
        """Search BST for a record - O(log n) average case"""
        position = self._search(self.root, target_id)

        if position is None:
            return None

        # Found the position, now read from file
        with open(self.filename, "r") as f:
            f.seek(position)
            record = f.readline().strip().split(",")

            # Handle different CSV formats gracefully
            result = {
                "id": record[0],
                "name": record[1] if len(record) > 1 else "N/A",
                "email": record[2] if len(record) > 2 else "N/A",
                "age": record[3] if len(record) > 3 else "N/A",
            }

            # Add city if it exists
            if len(record) > 4:
                result["city"] = record[4]

            return result

    def _search(self, node: Optional[BSTNode], key: int) -> Optional[int]:
        """Recursively search the BST"""
        if node is None:
            return None

        if key == node.key:
            return node.file_position
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def get_height(self) -> int:
        """Calculate tree height (useful for understanding balance)"""
        return self._get_height(self.root)

    def _get_height(self, node: Optional[BSTNode]) -> int:
        """Recursive height calculation"""
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))


def main():
    """Test the BST Database"""
    print("=" * 70)
    print("BST DATABASE - STANDALONE TEST")
    print("=" * 70)

    # Build the index
    print("\n[1] Building Index...")
    start_build = time.time()
    bst_db = BSTDatabase(filename="data.csv")
    build_time = time.time() - start_build
    print(f"    Build time: {build_time:.4f}s")
    print(f"    Tree height: {bst_db.get_height()} levels")

    # Test searches
    print("\n[2] Testing Searches...")
    print("-" * 70)
    test_ids = [1, 5000, 500000, 999999, 1000001]

    for target_id in test_ids:
        start = time.time()
        result = bst_db.find(target_id)
        elapsed = time.time() - start

        if result:
            print(
                f"  ID {target_id:7d}: ✓ Found in {elapsed*1000:.4f}ms - {result['name']}"
            )
        else:
            print(f"  ID {target_id:7d}: ✗ Not found ({elapsed*1000:.4f}ms)")

    print("\n" + "=" * 70)
    print("KEY POINTS:")
    print("=" * 70)
    print("• All BST nodes are stored in RAM")
    print("• Search is O(log n) on   average")
    print("• Tree height determines worst-case lookups")
    print("• For 1M records: ~80MB RAM used")
    print()
    print("⚠️  IMPORTANT: If tree height = number of records,")
    print("   your data is sorted and BST became a linked list!")
    print("   Real databases use balanced trees (AVL, Red-Black)")
    print("=" * 70)


if __name__ == "__main__":
    main()
