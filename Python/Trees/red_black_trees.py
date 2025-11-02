import enum


class Color(enum.Enum):
    RED = "RED"
    BLACK = "BLACK"


class RBNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.RED  # New nodes are always RED


class RedBlackTree:
    def __init__(self):
        # Create NIL node (represents all leaf nodes)
        self.NIL = RBNode(None)
        self.NIL.color = Color.BLACK

        self.root = self.NIL  # Start with empty tree (root is NIL)
        self.size = 0

    def insert(self, value):
        new_node = RBNode(data=value)
        # FIX 1: Initialize new node's children to NIL
        new_node.left = self.NIL
        new_node.right = self.NIL

        # Tree is empty
        if self.root == self.NIL:
            self.root = new_node
            new_node.color = Color.BLACK
            new_node.parent = self.NIL
            self.size += 1
            print(f"Inserted {value} as {new_node.color} node")
            return

        parent = None
        current = self.root

        # FIX 2: Change condition to check for NIL instead of None
        while current != self.NIL:
            parent = current
            if value < current.data:
                current = current.left
            else:
                current = current.right

        # FIX 3: Set parent pointer
        new_node.parent = parent

        # Insert new node
        if value < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.size += 1

        print(f"Inserted {value} as {new_node.color} node")
        # TODO: Next stage - add balancing
        self.fix_insert(new_node)

    def _rotate_left(self, x: RBNode):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        # Update x parent to point to y
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y

        elif x == x.parent.right:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, y: RBNode):
        x = y.left
        y.left = x.right

        # update the child of its new parents
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        # updateing the parent references
        if x.parent == self.NIL:
            self.root = x

        elif y.parent.left == y:
            y.parent.left = x

        elif y.parent.right == y:
            y.parent.right = x

        x.right = y
        y.parent = x

    def fix_insert(self, node):
        while node.parent != self.NIL and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == Color.RED:
                    # Case 1: Recolor
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED

                    node = node.parent.parent  # move it up to Grandparent
                    # Uncle is Black
                else:
                    # case 5: Left-Right
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    # Case 3: Left-Left
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == Color.RED:
                    # Case 2:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK

                    node.parent.parent.color = Color.RED
                    node = node.parent.parent

                else:
                    # Case 6: Right-Left
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)

                    # Case 4: Right-Right
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._rotate_left(node.parent.parent)

        # Case 0
        self.root.color = Color.BLACK

    def print_tree_simple(self, node=None, level=0, prefix="Root: "):
        """Simple tree visualization that shows colors"""
        if node is None:
            node = self.root
        if node == self.NIL:
            return

        color_str = "R" if node.color == Color.RED else "B"
        print(" " * (level * 4) + prefix + f"{node.data}({color_str})")

        if node.left != self.NIL:
            self.print_tree_simple(node.left, level + 1, "L--- ")
        if node.right != self.NIL:
            self.print_tree_simple(node.right, level + 1, "R--- ")


# Test Stage 1
if __name__ == "__main__":
    rbt = RedBlackTree()
    values = []
    for i in range(0, 11):
        values.append(i)

    print("=== STAGE 1: Basic Red-Black Structure ===")
    for value in values:
        rbt.insert(value)

    print(f"Size: {rbt.size}")
    print("\nTree structure (colors shown):")
    rbt.print_tree_simple()
