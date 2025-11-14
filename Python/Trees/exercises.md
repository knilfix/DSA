# Tree Practice Exercises

## Basic Traversals

### 1. InorderTraversal

Return the inorder traversal of a binary tree (Left -> Root -> Right).

**Function Signature:** `def inorderTraversal(root: TreeNode) -> List[int]`

**Example:**

```t
    1
     \
      2
     /
    3
Output: [1, 3, 2]
```

**Skills tested:** Recursive and iterative traversal, stack usage

---

### 2. PreorderTraversal

Return the preorder traversal of a binary tree (Root -> Left -> Right).

**Function Signature:** `def preorderTraversal(root: TreeNode) -> List[int]`

**Example:**

```t
    1
     \
      2
     /
    3
Output: [1, 2, 3]
```

**Skills tested:** DFS traversal order

---

### 3. PostorderTraversal

Return the postorder traversal of a binary tree (Left -> Right -> Root).

**Function Signature:** `def postorderTraversal(root: TreeNode) -> List[int]`

**Example:**

```t
    1
     \
      2
     /
    3
Output: [3, 2, 1]
```

**Skills tested:** Complex traversal order, stack manipulation

---

## Tree Properties

### 4. MaximumDepth

Find the maximum depth (height) of a binary tree.

**Function Signature:** `def maxDepth(root: TreeNode) -> int`

**Example:**

```t
    3
   / \
  9  20
    /  \
   15   7
Output: 3
```

**Skills tested:** Recursion, tree height calculation

---

### 5. MinimumDepth

Find the minimum depth from root to nearest leaf node.

**Function Signature:** `def minDepth(root: TreeNode) -> int`

**Example:**

```t
    3
   / \
  9  20
    /  \
   15   7
Output: 2 (path 3->9)
```

**Skills tested:** BFS or careful DFS, leaf node detection

---

### 6. CountNodes

Count the total number of nodes in a binary tree.

**Function Signature:** `def countNodes(root: TreeNode) -> int`

**Skills tested:** Complete tree traversal

---

### 7. SameTree

Check if two binary trees are identical (same structure and values).

**Function Signature:** `def isSameTree(p: TreeNode, q: TreeNode) -> bool`

**Example:**

```t
Tree 1:     Tree 2:
   1           1
  / \         / \
 2   3       2   3
Output: True
```

**Skills tested:** Simultaneous traversal, comparison logic

---

### 8. SymmetricTree

Check if a binary tree is a mirror of itself (symmetric around center).

**Function Signature:** `def isSymmetric(root: TreeNode) -> bool`

**Example:**

```t
    1
   / \
  2   2
 / \ / \
3  4 4  3
Output: True
```

**Skills tested:** Mirror comparison, helper functions

---

## Path & Sum Problems

### 9. PathSum

Check if there exists a root-to-leaf path with a given sum.

**Function Signature:** `def hasPathSum(root: TreeNode, targetSum: int) -> bool`

**Example:**

```t
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

targetSum = 22
Output: True (path 5->4->11->2)
```

**Skills tested:** DFS with accumulation, backtracking

---

### 10. PathSumII

Find all root-to-leaf paths where the sum equals target.

**Function Signature:** `def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]`

**Example:**

- Same tree as above, return `[[5,4,11,2], [5,8,4,5]]`

**Skills tested:** Path collection, backtracking

---

### 11. MaximumPathSum

Find the maximum path sum in a binary tree (path can start/end at any node).

**Function Signature:** `def maxPathSum(root: TreeNode) -> int`

**Example:**

```t
   -10
   /  \
  9   20
     /  \
    15   7
Output: 42 (path 15->20->7)
```

**Skills tested:** Post-order traversal, global vs local maximum

---

### 12. SumRootToLeafNumbers

Each root-to-leaf path represents a number. Find the total sum of all numbers.

**Function Signature:** `def sumNumbers(root: TreeNode) -> int`

**Example:**

```t
    1
   / \
  2   3
Numbers: 12, 13
Output: 25
```

**Skills tested:** Path accumulation, number building

---

## Binary Search Tree (BST)

### 13. ValidateBST

Check if a binary tree is a valid binary search tree.

**Function Signature:** `def isValidBST(root: TreeNode) -> bool`

**Example:**

```t
Valid BST:      Invalid BST:
    2               5
   / \             / \
  1   3           1   4
                     / \
                    3   6
```

**Skills tested:** BST property validation, range tracking

---

### 14. KthSmallestInBST

Find the kth smallest element in a BST.

**Function Signature:** `def kthSmallest(root: TreeNode, k: int) -> int`

**Example:**

```t
    3
   / \
  1   4
   \
    2
k = 1
Output: 1
```

**Skills tested:** Inorder traversal, early termination

---

### 15. LowestCommonAncestorBST

Find the lowest common ancestor of two nodes in a BST.

**Function Signature:** `def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode`

**Example:**

```t
       6
      / \
     2   8
    / \ / \
   0  4 7  9
     / \
    3   5

p = 2, q = 8
Output: 6
```

**Skills tested:** BST properties, ancestor search

---

### 16. InsertIntoBST

Insert a value into a BST and return the root.

**Function Signature:** `def insertIntoBST(root: TreeNode, val: int) -> TreeNode`

**Skills tested:** BST insertion, maintaining BST property

---

### 17. DeleteNodeInBST

Delete a node from a BST and return the root.

**Function Signature:** `def deleteNode(root: TreeNode, key: int) -> TreeNode`

**Skills tested:** BST deletion, three cases (leaf, one child, two children)

---

## Construction & Conversion

### 18. BuildTreeFromInorderPreorder

Construct a binary tree from inorder and preorder traversal arrays.

**Function Signature:** `def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode`

**Example:**

- Preorder: `[3, 9, 20, 15, 7]`
- Inorder: `[9, 3, 15, 20, 7]`
- Output: Construct the tree

**Skills tested:** Tree reconstruction, understanding traversal properties

---

### 19. BuildTreeFromInorderPostorder

Construct a binary tree from inorder and postorder traversal arrays.

**Function Signature:** `def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode`

**Skills tested:** Tree reconstruction from different traversals

---

### 20. SortedArrayToBST

Convert a sorted array to a height-balanced BST.

**Function Signature:** `def sortedArrayToBST(nums: List[int]) -> TreeNode`

**Example:**

- Input: `[-10, -3, 0, 5, 9]`
- Output: Balanced BST with root 0

**Skills tested:** Binary search pattern, balanced tree construction

---

### 21. FlattenBinaryTreeToLinkedList

Flatten a binary tree to a linked list in-place (using right pointers).

**Function Signature:** `def flatten(root: TreeNode) -> None`

**Example:**

```t
Input:      Output:
    1          1
   / \          \
  2   5          2
 / \   \          \
3   4   6          3
                    \
                     4
                      \
                       5
                        \
                         6
```

**Skills tested:** Tree to list conversion, in-place modification

---

## Advanced Problems

### 22. SerializeAndDeserializeBinaryTree

Design an algorithm to serialize a binary tree to a string and deserialize back.

**Methods to implement:**

- `serialize(root: TreeNode) -> str`
- `deserialize(data: str) -> TreeNode`

**Skills tested:** Tree serialization, null handling, BFS/DFS encoding

---

### 23. LowestCommonAncestor (General Tree)

Find the lowest common ancestor in a binary tree (not necessarily BST).

**Function Signature:** `def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode`

**Skills tested:** Post-order traversal, ancestor tracking

---

### 24. BinaryTreeMaximumPathSum

Find maximum path sum where path doesn't need to pass through root.

**Function Signature:** `def maxPathSum(root: TreeNode) -> int`

**Skills tested:** Complex recursion, global state tracking

---

### 25. DiameterOfBinaryTree

Find the longest path between any two nodes (may or may not pass through root).

**Function Signature:** `def diameterOfBinaryTree(root: TreeNode) -> int`

**Example:**

```t
    1
   / \
  2   3
 / \
4   5
Output: 3 (path 4->2->1->3 or 5->2->1->3)
```

**Skills tested:** Height calculation, diameter vs height distinction

---

### 26. VerticalOrderTraversal

Return the vertical order traversal of a binary tree (column by column, left to right).

**Function Signature:** `def verticalOrder(root: TreeNode) -> List[List[int]]`

**Example:**

```t
     3
    / \
   9  20
     /  \
    15   7

Output: [[9], [3,15], [20], [7]]
```

**Skills tested:** HashMap for columns, level-order traversal

---

### 27. RecoverBinarySearchTree

Two nodes of a BST are swapped by mistake. Recover the tree without changing structure.

**Function Signature:** `def recoverTree(root: TreeNode) -> None`

**Skills tested:** Inorder traversal, detecting violations, swapping

---

### 28. CountCompleteTreeNodes

Count nodes in a complete binary tree in less than O(n) time.

**Function Signature:** `def countNodes(root: TreeNode) -> int`

**Skills tested:** Complete tree properties, binary search optimization

---

## N-ary Tree Problems

### 29. MaxDepthNaryTree

Find the maximum depth of an N-ary tree.

**Function Signature:** `def maxDepth(root: Node) -> int`

**Skills tested:** Generalized tree traversal, handling multiple children

---

### 30. NaryTreeLevelOrderTraversal

Return the level order traversal of an N-ary tree.

**Function Signature:** `def levelOrder(root: Node) -> List[List[int]]`

**Skills tested:** BFS with variable children count

---

## Tips for Practice

1. **Draw First:** Always sketch the tree before coding
2. **Recursion Base Case:** Handle null nodes properly
3. **Return vs Modify:** Understand when to return values vs modify in-place
4. **Helper Functions:** Don't hesitate to write helper functions with extra parameters
5. **DFS vs BFS:** Choose based on problem requirements (level-order = BFS, paths = DFS)
6. **Global State:** Sometimes you need a class variable or wrapper for tracking

## Common Tree Patterns

- **DFS Patterns:** Preorder, Inorder, Postorder
- **BFS Pattern:** Level-order traversal using queue
- **Divide & Conquer:** Solve for left/right subtrees, combine results
- **Path Tracking:** Accumulate values as you traverse
- **BST Properties:** Left < Root < Right
- **Tree Construction:** Use traversal arrays or sorted data
- **Lowest Common Ancestor:** Post-order with boolean returns
- **Serialization:** BFS with null markers or preorder with delimiters
