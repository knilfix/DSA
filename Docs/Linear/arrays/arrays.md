# Arrays

## 🧩 Definition

An array is a contiguous block of memory that stores elements of the same type, accessible via an index.

## 💡 Core Idea

Arrays exist to provide **constant-time access** to elements by their index, making sequential data storage and iteration efficient.
They trade off flexibility (fixed size in low-level languages) for speed and predictability.

## ⚙️ Key Operations

| Operation    | Description                     | Time Complexity |
| ------------ | ------------------------------- | --------------- |
| access(i)    | Retrieve element at index *i*   | O(1)            |
| insert(i, x) | Insert element *x* at index *i* | O(n)            |
| delete(i)    | Remove element at index *i*     | O(n)            |
| search(x)    | Find element *x* in the array   | O(n)            |

## 🧱 Internal Concept

Arrays store elements in **contiguous memory addresses**.
This allows direct computation of an element’s address:
`address = base_address + (index * element_size)`

In low-level languages (like C), this also means arrays cannot grow dynamically — resizing requires allocating new memory and copying old data.
In higher-level languages (like Python lists), dynamic resizing is handled under the hood using *amortized doubling*.

## 🧭 Use Cases

* Sequential storage (buffers, matrices)
* Index-based access (lookup tables)
* Building blocks for other DSAs (heaps, hash tables)
* Implementing stacks, queues, or dynamic arrays

## 🧮 Complexity Overview

| Operation        | Time | Space |
| ---------------- | ---- | ----- |
| Access           | O(1) | O(1)  |
| Search           | O(n) | O(1)  |
| Insert/Delete    | O(n) | O(1)  |
| Resize (dynamic) | O(n) | O(n)  |

## 🧰 Implementation References

* **Python:** [../Python/Heaps/max_heap.py](../Python/Heaps/max_heap.py)
  *(Uses array-based storage)*
* **C:** [../C/LinearDataStructures/dynamic_arrays.c](../C/LinearDataStructures/dynamic_arrays.c)

## 🧠 Notes & Insights

* Think of arrays as the “bare metal” of data storage — everything else builds on top of them.
* In C, arrays decay into pointers, while in Python they behave like resizable lists.
* Memory locality makes arrays cache-friendly and fast in real applications.
