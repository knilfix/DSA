# Binary Trees

## 🧩 **Definition**

A **Binary Tree** is a hierarchical data structure in which each node has at most **two children** — a **left child** and a **right child**. It forms the foundation of many advanced data structures such as **heaps**, **binary search trees**, and **red-black trees**.

---

## 💡 **Core Idea**

The main goal of a binary tree is to represent **hierarchical relationships** in data while allowing efficient traversal and organization.
It’s a flexible structure that can represent order, priority, or structure — depending on how you constrain it (e.g., BSTs add sortedness).

---

## ⚙️ **Key Operations**

| Operation         | Description                                          | Time Complexity |
| ----------------- | ---------------------------------------------------- | --------------- |
| `insert(value)`   | Adds a new node in a specific position               | O(n)            |
| `search(value)`   | Finds a node with the given value                    | O(n)            |
| `delete(value)`   | Removes a node                                       | O(n)            |
| `traverse(order)` | Visit nodes (Preorder/Inorder/Postorder/Level-order) | O(n)            |

---

## 🧱 **Internal Concept**

A **binary tree** is made up of **nodes**, each containing:

* A **data value**
* A pointer/reference to a **left child**
* A pointer/reference to a **right child**

```t
           [A]
          /   \
        [B]   [C]
       / \     \
     [D] [E]   [F]
```

Each node acts as the root of its own subtree.
There is **no specific ordering rule** in a generic binary tree (unlike BSTs).
Traversal defines how you visit and process nodes — e.g.:

* **Preorder (Root → Left → Right)**
* **Inorder (Left → Root → Right)**
* **Postorder (Left → Right → Root)**
* **Level-order (BFS style)**

---

## 🧭 **Use Cases**

* Representing hierarchical data (e.g., organizational charts, XML/HTML DOM)
* Expression trees (used in compilers)
* Parsing syntax or structured data
* Underlying structure for Binary Search Trees and Heaps

---

## 🧮 **Complexity Overview**

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(n)    | O(n)  |
| Search    | O(n)    | O(n)  |
| Delete    | O(n)    | O(n)  |
| Traversal | O(n)    | O(n)  |
| Space     | O(n)    | O(n)  |

---

## 🧰 **Implementation References**

* **Python:** [../Python/Trees/binary_tree.py](../Python/Trees/binary_tree.py)
* **C:** [../C/NonLinearDataStructures/Trees/binary_tree.c](../C/NonLinearDataStructures/Trees/binary_tree.c)

---

## 🧠 **Notes & Insights**

* Binary trees are **not inherently sorted** — they just maintain a structure.
* Their efficiency depends heavily on their **shape** (balanced vs skewed).
* Almost every non-linear data structure builds upon this base concept.
* Understanding **tree traversal** is key — it underpins all advanced tree algorithms.

---
