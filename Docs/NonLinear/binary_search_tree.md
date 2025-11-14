# Binary Search Trees

## 🧩 **Definition**

A **Binary Search Tree (BST)** is a binary tree with an ordering property:
For every node,

* **Left subtree** contains values *less than* the node’s key
* **Right subtree** contains values *greater than* the node’s key

This rule applies recursively to every subtree in the tree.

---

### 💡 **Core Idea**

The goal of a BST is to enable **fast lookup, insertion, and deletion** by maintaining a *sorted structure* within a tree form.
By keeping elements ordered as you insert them, you can search efficiently — just like binary search on a sorted array, but dynamically.

---

### ⚙️ **Key Operations**

| Operation             | Description                          | Time Complexity              |
| --------------------- | ------------------------------------ | ---------------------------- |
| `insert(value)`       | Adds a node to maintain BST order    | O(log n) average, O(n) worst |
| `search(value)`       | Finds if a value exists in the tree  | O(log n) average, O(n) worst |
| `delete(value)`       | Removes a node and restructures tree | O(log n) average, O(n) worst |
| `inorder_traversal()` | Returns sorted order of elements     | O(n)                         |

---

### 🧱 **Internal Concept**

Each node in a BST contains:

* A **key/value**
* A reference to a **left child**
* A reference to a **right child**

The BST property:

```t
For any node N:
    all(left_subtree) < N.key < all(right_subtree)
```

Example:

```t
          [8]
         /   \
       [3]   [10]
      /  \      \
    [1]  [6]    [14]
        /  \    /
      [4] [7] [13]
```

* Searching for `7` only visits `[8] → [3] → [6] → [7]` — efficient and directional.
* Deletion cases:

  * Node has **no children** → remove directly
  * Node has **one child** → replace with child
  * Node has **two children** → replace with **inorder successor/predecessor**

---

### 🧭 **Use Cases**

* Maintaining sorted dynamic data
* Implementing ordered maps or sets
* Searching within ranges
* Autocomplete or prefix-matching (foundation for tries)
* In-memory indexing (e.g., database internals)

---

### 🧮 **Complexity Overview**

| Operation | Average  | Worst (unbalanced) |
| --------- | -------- | ------------------ |
| Insert    | O(log n) | O(n)               |
| Search    | O(log n) | O(n)               |
| Delete    | O(log n) | O(n)               |
| Traversal | O(n)     | O(n)               |
| Space     | O(n)     | O(n)               |

---

### 🧰 **Implementation References**

* **Python:** [../Python/playground/bst.py](../Python/playground/bst.py)
* **C:** [../C/NonLinearDataStructures/Trees/bst.c](../C/NonLinearDataStructures/Trees/bst.c)

---

### 🧠 **Notes & Insights**

* A BST’s performance **depends on balance** — a skewed BST degrades to a linked list.
* **Balanced trees** (AVL, Red-Black, B-trees) were invented to solve that issue.
* The **inorder traversal** of any BST always yields a *sorted list* of keys.
* BSTs are simple yet powerful — almost every advanced tree builds on their principles.

---

Would you like me to jump straight into **red_black_tree.md** now (since it extends this concept and shows how balance is maintained)?
