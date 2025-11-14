# 🧮 Complexity Cheatsheet

A concise reference for time and space complexities of common data structures and algorithms.

---

## ⚡ Big-O Basics

| Complexity     | Name         | Description                                            |
| -------------- | ------------ | ------------------------------------------------------ |
| **O(1)**       | Constant     | Does not depend on input size                          |
| **O(log n)**   | Logarithmic  | Growth slows as input increases (e.g., binary search)  |
| **O(n)**       | Linear       | Grows directly with input size                         |
| **O(n log n)** | Linearithmic | Common in efficient sorting algorithms                 |
| **O(n²)**      | Quadratic    | Nested loops or pairwise comparisons                   |
| **O(2ⁿ)**      | Exponential  | Explodes with input size (e.g., brute force recursion) |
| **O(n!)**      | Factorial    | Permutation-heavy algorithms                           |

---

## 🧩 Common Data Structures

### **Arrays**

| Operation              | Time           | Notes                              |
| ---------------------- | -------------- | ---------------------------------- |
| Access                 | O(1)           | Direct index access                |
| Search                 | O(n)           | Linear scan                        |
| Insert/Delete (end)    | O(1) amortized | Dynamic arrays (e.g., Python list) |
| Insert/Delete (middle) | O(n)           | Shifting required                  |

### **Linked Lists**

| Operation               | Time               | Notes                 |
| ----------------------- | ------------------ | --------------------- |
| Access (by index)       | O(n)               | Must traverse         |
| Search                  | O(n)               | Sequential traversal  |
| Insert/Delete (at head) | O(1)               | Direct pointer change |
| Insert/Delete (at tail) | O(1) if tail known | Else O(n)             |

### **Stacks & Queues**

| Operation               | Time | Notes             |
| ----------------------- | ---- | ----------------- |
| Push/Pop (Stack)        | O(1) | LIFO              |
| Enqueue/Dequeue (Queue) | O(1) | FIFO              |
| Peek                    | O(1) | Top/front element |

### **Hash Maps / Hash Tables**

| Operation | Average | Worst | Notes                        |
| --------- | ------- | ----- | ---------------------------- |
| Insert    | O(1)    | O(n)  | Collision-heavy case         |
| Search    | O(1)    | O(n)  | Same as above                |
| Delete    | O(1)    | O(n)  | Depends on hash distribution |

### **Heaps**

| Operation       | Time     | Notes        |
| --------------- | -------- | ------------ |
| Insert          | O(log n) | Bubble-up    |
| Extract Min/Max | O(log n) | Heapify-down |
| Peek            | O(1)     | Root access  |

### **Trees (Binary Search Tree)**

| Operation | Average  | Worst | Notes                 |
| --------- | -------- | ----- | --------------------- |
| Insert    | O(log n) | O(n)  | Worst when unbalanced |
| Search    | O(log n) | O(n)  | Same                  |
| Delete    | O(log n) | O(n)  | Same                  |

### **Balanced Trees (AVL, Red-Black)**

| Operation | Time     | Notes                            |
| --------- | -------- | -------------------------------- |
| Insert    | O(log n) | Rebalancing ensures height log n |
| Search    | O(log n) |                                  |
| Delete    | O(log n) |                                  |

### **Graphs**

| Operation                  | Time       | Notes                     |
| -------------------------- | ---------- | ------------------------- |
| BFS / DFS                  | O(V + E)   | Visits all vertices/edges |
| Dijkstra’s (with min-heap) | O(E log V) | Shortest path             |
| Topological Sort           | O(V + E)   | Directed acyclic graphs   |

---

## 🧠 Sorting Algorithms

| Algorithm      | Best       | Average    | Worst      | Space    | Stable | Notes                                   |
| -------------- | ---------- | ---------- | ---------- | -------- | ------ | --------------------------------------- |
| Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅      | Educational, not practical              |
| Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | ✅      | Great for small or nearly-sorted arrays |
| Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | ❌      | Always quadratic                        |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅      | Divide and conquer                      |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | ❌      | In-place, but pivot-dependent           |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | ❌      | Based on heap structure                 |
| Counting Sort  | O(n + k)   | O(n + k)   | O(n + k)   | O(k)     | ✅      | Works for integers, limited range       |

---

## 💾 Space Complexity Overview

| Data Structure / Algorithm | Space                              |
| -------------------------- | ---------------------------------- |
| Array / List               | O(n)                               |
| Linked List                | O(n)                               |
| Stack / Queue              | O(n)                               |
| Hash Map                   | O(n)                               |
| Binary Tree                | O(n)                               |
| Graph                      | O(V + E)                           |
| Merge Sort                 | O(n)                               |
| Quick Sort                 | O(log n)                           |
| Dynamic Programming        | O(n) to O(n²) depending on problem |

---

## 🔍 Quick Rules of Thumb

* If you see **nested loops**, you’re likely at O(n²).
* If you divide input in half each time (binary search, heapify), you’re around **O(log n)**.
* If you process every node in a tree or graph, expect **O(n)** or **O(V + E)**.
* **Recursion** often adds space overhead proportional to recursion depth.
* **Hash-based structures** are near-constant time until collisions dominate.

---

## 🧩 Related Resources

* [Big O Cheatsheet](https://www.bigocheatsheet.com/)
* [MIT 6.006 – Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)
* [Python Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity)
