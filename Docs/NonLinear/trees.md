
# 🧩 **Definition**

A **Tree** is a hierarchical data structure made up of **nodes**, where each node stores data and links to its **children**.
It starts from a single **root** node, and each child forms a **subtree**.
Unlike linear structures, trees model **hierarchical relationships** — perfect for representing systems with parent–child dependencies.

---

## 💡 **Core Idea**

Trees exist to represent **hierarchical data** and to enable **faster search and organization** compared to unsorted linear structures.
They form the foundation for:

* Hierarchical storage (filesystems, DOM)
* Search trees (BST, AVL, RBT)
* Heaps (for priority and scheduling)
* Parsing and structured data (syntax trees, JSON)

Essentially, trees generalize the idea of “sorted lists” into “sorted hierarchies.”

---

## ⚙️ **Key Operations**

| Operation         | Description                                | Time Complexity |
| ----------------- | ------------------------------------------ | --------------- |
| `insert(node)`    | Adds a new node in the structure           | O(log n) avg    |
| `delete(node)`    | Removes a node while maintaining structure | O(log n) avg    |
| `search(value)`   | Finds a specific value                     | O(log n) avg    |
| `traverse(order)` | Visits nodes in a specific order           | O(n)            |
| `height()`        | Returns depth of tree                      | O(n)            |

> **Note:** Exact complexity depends on tree type — e.g., balanced vs unbalanced.

---

## 🧱 **Internal Concept**

A **Tree** is a set of connected nodes with these properties:

* One node is the **root**
* Every node (except the root) has **one parent**
* Nodes may have **zero or more children**
* There are **no cycles**

```t
            [Root]
            /    \
         [A]      [B]
        /  \      / \
      [C] [D]  [E] [F]
```

**Terminology:**

* **Root** → topmost node
* **Leaf** → node with no children
* **Parent / Child** → relationship between nodes
* **Subtree** → a tree within a tree
* **Depth / Height** → distance from root or leaves

---

## 🧭 **Use Cases**

* Hierarchical data: XML/HTML DOM, file systems
* Search optimization: BSTs, Red-Black Trees
* Priority systems: Heaps
* Network routing or game trees (AI)
* Expression trees in compilers/interpreters

---

## 🧮 **Complexity Overview**

| Operation | Average  | Worst (Unbalanced) |
| --------- | -------- | ------------------ |
| Insert    | O(log n) | O(n)               |
| Search    | O(log n) | O(n)               |
| Delete    | O(log n) | O(n)               |
| Traversal | O(n)     | O(n)               |
| Space     | O(n)     | O(n)               |

---

## 🧰 **Implementation References**

* **Python:**

  * [../Python/Trees/binary_tree.py](../Python/Trees/binary_tree.py)
  * [../Python/playground/bst.py](../Python/playground/bst.py)
  * [../Python/playground/red_black_tree.py](../Python/playground/red_black_tree.py)
  * [../Python/Heaps/max_heap.py](../Python/Heaps/max_heap.py)

* **C:**

  * [../C/NonLinearDataStructures/Trees/binary_tree.c](../C/NonLinearDataStructures/Trees/binary_tree.c)
  * [../C/NonLinearDataStructures/Trees/bst.c](../C/NonLinearDataStructures/Trees/bst.c)
  * [../C/NonLinearDataStructures/Trees/red_black_tree.c](../C/NonLinearDataStructures/Trees/red_black_tree.c)
  * [../C/NonLinearDataStructures/Trees/heap.c](../C/NonLinearDataStructures/Trees/heap.c)

---

## 🧠 **Notes & Insights**

* **Trees = hierarchical data + structure constraints.**
* Every specialized tree (BST, RBT, Heap) just enforces *extra rules* on top of this base.
* Traversals define the logic for all processing — e.g. inorder (for sorting), postorder (for cleanup).
* Balancing is what transforms basic trees into high-performance data structures.
* Understanding this base concept makes *any* advanced data structure far easier to grasp.

---
