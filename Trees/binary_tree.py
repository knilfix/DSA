from collections import deque
import random


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = TreeNode(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
            return

        current = self.head
        parent = None

        while current:
            parent = current
            if data > current.data:
                current = current.right
            else:
                current = current.left
        if parent:

            if data > parent.data:
                parent.right = new_node
            else:
                parent.left = new_node

            self.size += 1

    def search(self, item):
        current = self.head
        while current:
            if item == current.data:
                return True
            if item > current.data:
                current = current.right  # This could make current None
            else:
                current = current.left  # This could make current None
        return False

    def find_min(self, current_node):

        if self.is_empty():
            return

        current = current_node

        while current.left:
            current = current.left

        return current

    def find_max(self, current_node):
        if self.is_empty():
            return

        current = current_node
        while current.right:
            current = current.right

        return current

    def breadth_first_search(self):
        if self.is_empty():
            print("Tree is Empty")
            return

        queue = deque([self.head])

        while queue:
            node = queue.popleft()
            if node:
                print(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def print_tree_level(self):
        if self.is_empty():
            print("(Tree is empty)")
            return

        queue = deque([(self.head, 0)])  # (node, level)
        current_level = -1

        while queue:
            node, level = queue.popleft()

            if level != current_level:
                print()  # New line for new level
                print(f"Level {level}: ", end="")
                current_level = level

            if node:

                print(node.data, end=" ")  # Print node on same line

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        print()  # Final newline

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if self.is_empty():
            print("(Tree is empty)")
            return

        if node is None:
            node = self.head

        if node:

            # Print the current node with indentation
            print(" " * (level * 4) + prefix + str(node.data))

            # Recursively print left and right children
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")

    # Traversals
    def in_order_traversal(self, node):

        if node is None:
            return

        self.in_order_traversal(node.left)
        print(node.data)
        self.in_order_traversal(node.right)

    def is_empty(self):
        return self.head == None

    def delete(self, data):
        self.head = self._delete_recursive(self.head, data)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.data:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.data:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Case 2: Node with two children
            temp_node = self.find_min(current_node.right)
            if temp_node is None:
                raise ValueError("Unexpected: right subtree is empty")
            current_node.data = temp_node.data
            current_node.right = self._delete_recursive(
                current_node.right, temp_node.data
            )

        return current_node


def generate_numbers(count=100, min_val=1, max_val=1000, unique=False):
    """
    Generates a list of random numbers for testing.

    Parameters:
    count (int): How many numbers to generate
    min_val (int): Minimum value (inclusive)
    max_val (int): Maximum value (inclusive)
    unique (bool): Whether all numbers should be unique

    Returns:
    list: List of random numbers
    """
    if unique:
        if (max_val - min_val + 1) < count:
            raise ValueError(
                "Cannot generate unique numbers: range too small for count"
            )
        return random.sample(range(min_val, max_val + 1), count)
    else:
        return [random.randint(min_val, max_val) for _ in range(count)]


def main():
    bst = BinarySearchTree()

    print("=== Phase 1: Testing Empty Tree ===")
    print("Is empty?", bst.is_empty())
    bst.breadth_first_search()  # Should print "Tree is Empty"
    print()

    print("=== Phase 2: Inserting Nodes & BFS ===")
    nodes_to_insert = generate_numbers(count=99)
    for data in nodes_to_insert:
        bst.insert(data)
    bst.insert(66)
    root = bst.head

    print("Size of tree:", bst.size)
    print("Is empty?", bst.is_empty())
    print()

    print("Searching for 66:", bst.search(66))
    bst.print_tree_level()
    bst.delete(66)
    bst.print_tree_level()
    print("Searching for 66:", bst.search(66))
    bst.in_order_traversal(root)
    print()

    min_node = bst.find_min(root)
    if min_node is not None:
        print("Minimum value in BST:", min_node.data)
    else:
        print("Minimum value in BST: None (empty tree)")

    max_node = bst.find_max(root)
    if max_node is not None:
        print("Maximum value in BST:", max_node.data)
    else:
        print("Maximum value in BST: None (empty tree)")
