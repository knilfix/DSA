# Queues

## 🧩 Definition

A queue is a linear data structure that follows the **First In, First Out (FIFO)** principle — the first element added is the first one removed.

## 💡 Core Idea

Queues exist to model **real-world waiting lines** and manage data in the order it arrives.
They’re perfect for handling **sequential processing**, task scheduling, and buffering.

## ⚙️ Key Operations

| Operation  | Description                   | Time Complexity |
| ---------- | ----------------------------- | --------------- |
| enqueue(x) | Add element *x* to the rear   | O(1)            |
| dequeue()  | Remove element from the front | O(1)            |
| peek()     | View the front element        | O(1)            |
| is_empty() | Check if queue is empty       | O(1)            |

## 🧱 Internal Concept

Queues can be implemented using:

* **Arrays (Circular Queues):** wrap around using modulo arithmetic
* **Linked Lists:** dynamic memory with front and rear pointers

Example (circular array):

```
Front → [A, B, C, D] ← Rear
Enqueue(E): [A, B, C, D, E]
Dequeue(): removes A → Front moves forward
```

### Circular Queue Visualization

```
Indices: 0 1 2 3 4
Queue:   [E, _, C, D, E]
front=2, rear=0  (wrapped)
```

## 🧭 Use Cases

* Task scheduling (CPU, printer queues)
* Breadth-first search (BFS)
* Producer-consumer buffering
* Network packet management
* Message passing systems

## 🧮 Complexity Overview

| Operation             | Time | Space |
| --------------------- | ---- | ----- |
| Enqueue               | O(1) | O(1)  |
| Dequeue               | O(1) | O(1)  |
| Peek                  | O(1) | O(1)  |
| Search (non-standard) | O(n) | O(1)  |

## 🧰 Implementation References

* **Python:** [../Python/Queue/queue.py](../Python/Queue/queue.py)
  *(Simple queue implementation)*
* **C:** [../C/LinearDataStructures/queue.c](../C/LinearDataStructures/queue.c)

## 🧠 Notes & Insights

* Think of queues as **pipelines** — data enters one end and exits the other in order.
* **Circular queues** fix wasted space in basic array queues.
* Variants include **deque** (double-ended queue) and **priority queue** (ordered by priority).
* Used everywhere from **OS process management** to **AI pathfinding**.
