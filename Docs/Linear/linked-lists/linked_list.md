# Linked Lists

## 🧩 Definition

A linked list is a linear data structure made up of **nodes**, where each node stores data and a reference (or pointer) to the next node in the sequence.

## 💡 Core Idea

Linked lists exist to allow **dynamic memory allocation and efficient insertions/deletions** without needing contiguous memory, unlike arrays.
They trade off random access speed for structural flexibility.

## ⚙️ Key Operations

| Operation       | Description                 | Time Complexity              |
| --------------- | --------------------------- | ---------------------------- |
| insert_front(x) | Add element *x* at the head | O(1)                         |
| insert_end(x)   | Add element *x* at the tail | O(n) or O(1) if tail tracked |
| delete(x)       | Remove node containing *x*  | O(n)                         |
| search(x)       | Find node with value *x*    | O(n)                         |
| traverse()      | Visit each node in order    | O(n)                         |

## 🧱 Internal Concept

Each node contains:

```
[data | next]
```

For a doubly linked list:

```
[prev | data | next]
```

Nodes are dynamically allocated on the heap.
Links connect them, forming a chain that can grow or shrink easily.

In memory:

```
head → [A|•] → [B|•] → [C|null]
```

Since elements aren’t contiguous, random access requires traversal from the head node.

## 🧭 Use Cases

* Dynamic memory-based collections (stacks, queues)
* Undo/redo features (text editors)
* Implementing LRU caches
* Polynomial representation, adjacency lists (graphs)

## 🧮 Complexity Overview

| Operation                   | Time | Space |
| --------------------------- | ---- | ----- |
| Access (by index)           | O(n) | O(1)  |
| Search                      | O(n) | O(1)  |
| Insert/Delete (at head)     | O(1) | O(1)  |
| Insert/Delete (middle/tail) | O(n) | O(1)  |

## 🧰 Implementation References

* **Python:** [../Python/Linked_List/linked_list.py](../Python/Linked_List/linked_list.py)
  *(Singly linked list implementation)*
* **C:** [../C/LinearDataStructures/linked_lists.c](../C/LinearDataStructures/linked_lists.c)

## 🧠 Notes & Insights

* Perfect when memory fragmentation makes contiguous allocation difficult.
* Traversal can’t go backward in singly linked lists — doubly linked ones solve this at a small memory cost.
* Think of it like a **train of nodes**: changing one connection can rearrange or remove entire sections efficiently.
* Great conceptual bridge between pointers and dynamic memory management.
