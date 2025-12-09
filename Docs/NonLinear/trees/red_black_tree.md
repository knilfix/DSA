# Red Black Trees

### 🧩 **Definition**

A **Red-Black Tree (RBT)** is a **self-balancing binary search tree** where each node stores an extra bit of information — its **color** (either red or black).
The colors are used to ensure the tree remains **approximately balanced**, guaranteeing O(log n) operations for insertion, deletion, and search.

---

### 💡 **Core Idea**

The Red-Black Tree improves upon the standard BST by automatically **restructuring itself** during inserts and deletions.
It keeps the height logarithmic through a set of color-based **invariants** that prevent the tree from becoming skewed — all while staying simpler than AVL trees.

---

### ⚙️ **Key Operations**

| Operation       | Description                                             | Time Complexity |
| --------------- | ------------------------------------------------------- | --------------- |
| `insert(value)` | Inserts a node and rebalances via color flips/rotations | O(log n)        |
| `delete(value)` | Removes a node and rebalances                           | O(log n)        |
| `search(value)` | Finds if a key exists                                   | O(log n)        |
| `traverse()`    | Visit nodes (inorder, preorder, etc.)                   | O(n)            |

---

### 🧱 **Internal Concept**

Each node contains:

* A **key/value**
* Pointers to **left** and **right** children
* A **color** (Red or Black)
* A pointer to its **parent**

#### **Properties (must always hold):**

1. Every node is either **red** or **black**.
2. The **root** is always **black**.
3. All **leaves (NIL nodes)** are **black**.
4. If a node is **red**, both its children are **black** (no two reds in a row).
5. Every path from a node to its descendant NIL nodes has the **same number of black nodes**.

Example (conceptual):

```
         [10B]
        /     \
     [5R]     [15R]
     /  \     /   \
  [2B] [7B] [12B] [18B]
```

After insertions or deletions, **violations** of these properties are corrected using:

* **Rotations** (left or right)
* **Recoloring** (flipping node colors)

These ensure balance is restored locally, without rebalancing the whole tree.

---

### 🔧 **Insertion Fix Cases**

After inserting a new red node, violations of the Red-Black properties are fixed based on the **color of the parent and uncle** and the relative position of the node:

| Case  | Situation                                                                            | Action                                                                                                            |
| ----- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **1** | Node is root                                                                         | Recolor node to black                                                                                             |
| **2** | Parent is black                                                                      | Tree is still valid → do nothing                                                                                  |
| **3** | Parent is red, Uncle is red                                                          | Recolor Parent & Uncle to black, Grandparent to red; move current node pointer to Grandparent and continue fixing |
| **4** | Parent is red, Uncle is black/NIL, Node is left child of left parent (Left-Left)     | Right rotate Grandparent, swap colors of Parent & Grandparent                                                     |
| **5** | Parent is red, Uncle is black/NIL, Node is right child of left parent (Left-Right)   | Left rotate Parent → becomes Left-Left → Right rotate Grandparent, swap colors                                    |
| **6** | Parent is red, Uncle is black/NIL, Node is right child of right parent (Right-Right) | Left rotate Grandparent, swap colors of Parent & Grandparent                                                      |
| **7** | Parent is red, Uncle is black/NIL, Node is left child of right parent (Right-Left)   | Right rotate Parent → becomes Right-Right → Left rotate Grandparent, swap colors                                  |

**Notes:**

* Cases 4–7 involve **rotations** to restore balance.
* Always ensure the **root remains black** after fixes.
* Cases are mirrored depending on whether the parent is a left or right child.

---

### 🧭 **Use Cases**

* Implementing **ordered associative containers** (like `std::map` or `TreeMap`)
* **Databases and file systems** (underpinning indexing structures)
* **Memory management** (Linux kernel’s `rbtrees` manage VM regions)
* **Scheduling systems** where ordered retrievals are required

---

### 🧮 **Complexity Overview**

| Operation | Average  | Worst    |
| --------- | -------- | -------- |
| Insert    | O(log n) | O(log n) |
| Search    | O(log n) | O(log n) |
| Delete    | O(log n) | O(log n) |
| Traversal | O(n)     | O(n)     |
| Space     | O(n)     | O(n)     |

---

### 🧰 **Implementation References**

* **Python:** [../Python/playground/red_black_tree.py](../Python/playground/red_black_tree.py)
* **C:** [../C/NonLinearDataStructures/Trees/red_black_tree.c](../C/NonLinearDataStructures/Trees/red_black_tree.c)

---

### 🧠 **Notes & Insights**

* Red-Black Trees guarantee that no path is more than **twice as long** as any other — this ensures near-perfect balance.
* They’re slightly slower to insert than AVL trees but faster in practice for mixed workloads (insert/search/delete).
* The **coloring logic** gives the structure flexibility — rotations fix local imbalance efficiently.
* Understanding RBTs deeply gives you insight into **real-world ordered data structures**, since they’re used almost everywhere from C++ STL to the Linux kernel.
