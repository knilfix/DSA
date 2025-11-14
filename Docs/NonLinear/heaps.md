# Heap

## 🧩 **Definition**

A **Heap** is a specialized binary tree–based data structure that satisfies the *heap property*:

* In a **max-heap**, every parent node is greater than or equal to its children.
* In a **min-heap**, every parent node is less than or equal to its children.

---

## 💡 **Core Idea**

Heaps exist to efficiently retrieve and remove the **minimum or maximum element** in *O(log n)* time, without needing to fully sort the data.
They’re the backbone for **priority queues**, **heap sort**, and **graph algorithms** like Dijkstra’s shortest path.

---

## ⚙️ **Key Operations**

| Operation                         | Description                                     | Time Complexity |
| --------------------------------- | ----------------------------------------------- | --------------- |
| `insert(x)`                       | Adds an element while maintaining heap property | O(log n)        |
| `extract_min()` / `extract_max()` | Removes the smallest/largest element            | O(log n)        |
| `peek()`                          | Returns min/max without removing                | O(1)            |
| `heapify(array)`                  | Builds a heap from an array                     | O(n)            |
| `search(x)`                       | Searches for an element                         | O(n)            |

---

## 🧱 **Internal Concept**

Heaps are usually implemented using **arrays**, not pointers.
For any node at index `i`:

* **Left child:** `2*i + 1`
* **Right child:** `2*i + 2`
* **Parent:** `(i - 1) // 2`

Insertion and removal both rely on **heapify up** and **heapify down** operations, which swap elements along the tree until the heap property is restored.

```t
        10
       /  \
      5    3
     / \  / \
    2  4 1  ( )
```

---

## 🧭 **Use Cases**

* Implementing **priority queues**
* **Heap sort**
* **Graph algorithms** (Dijkstra, Prim)
* Real-time systems (e.g., scheduling by priority)
* Stream median finding

---

## 🧮 **Complexity Overview**

| Operation  | Average  | Worst    |
| ---------- | -------- | -------- |
| Insertion  | O(log n) | O(log n) |
| Deletion   | O(log n) | O(log n) |
| Peek (top) | O(1)     | O(1)     |
| Build Heap | O(n)     | O(n)     |
| Space      | O(n)     | O(n)     |

---

## 🧰 **Implementation References**

* **Python:** [../Python/Heaps/max_heap.py](../Python/Heaps/max_heap.py), [../Python/Heaps/min_heap.py](../Python/Heaps/min_heap.py)
* **C:** [../C/NonLinearDataStructures/Trees/heap.c](../C/NonLinearDataStructures/Trees/heap.c)

---

## 🧠 **Notes & Insights**

* The heap is **not sorted**, just *partially ordered*.
* The array-based layout is cache-friendly and simple.
* A *priority queue* is often just a **heap with an API wrapper**.
* **Binary heaps** are most common, but there are also Fibonacci and Binomial heaps for advanced scenarios.

---
