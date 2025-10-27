from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_traversal(root):
    if root is None:
        print("Tree is Empty")
        return []

    elements = []

    queue = deque([root])
    while queue:
        node = queue.popleft()
        elements.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return elements


def bfs_search(node, value):
    if root is None:
        print("Tree is Empty")
        return False

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == value:
            return True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("BFS Traversal:", bfs_traversal(root))  # [4, 2, 6, 1, 3, 5, 7]
print("Search for 5:", bfs_search(root, 5))  # True
print("Search for 9:", bfs_search(root, 9))  # False
