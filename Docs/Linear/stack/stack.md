# Stacks

## 🧩 Definition

A stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle — the last element added is the first one removed.

## 💡 Core Idea

Stacks exist to model problems where **reversal or nesting** is key — like function calls, undo operations, and syntax parsing.
They provide a controlled way to store temporary states and backtrack efficiently.

## ⚙️ Key Operations

| Operation  | Description                              | Time Complexity |
| ---------- | ---------------------------------------- | --------------- |
| push(x)    | Add element *x* to the top               | O(1)            |
| pop()      | Remove the top element                   | O(1)            |
| peek()     | View the top element without removing it | O(1)            |
| is_empty() | Check if stack is empty                  | O(1)            |

## 🧱 Internal Concept

Stacks can be implemented using:

* **Arrays / Lists:** fixed or dynamic resizing
* **Linked Lists:** nodes linked in LIFO order

Example (array-based):

```
Top → [E, D, C, B, A]
Push(F) → [F, E, D, C, B, A]
Pop() → removes F
```

Each operation happens at one end — the **top** — making it efficient and predictable.

## 🧭 Use Cases

* Function call stacks (recursion, stack frames)
* Undo/redo mechanisms
* Expression evaluation (postfix/prefix)
* Balanced parentheses checking
* Browser navigation (back/forward)

## 🧮 Complexity Overview

| Operation             | Time | Space |
| --------------------- | ---- | ----- |
| Push                  | O(1) | O(1)  |
| Pop                   | O(1) | O(1)  |
| Peek                  | O(1) | O(1)  |
| Search (non-standard) | O(n) | O(1)  |

## 🧰 Implementation References

* **Python:** [../Python/Stack/stack.py](../Python/Stack/stack.py)
  *(Array-based implementation)*
* **C:** [../C/LinearDataStructures/stack.c](../C/LinearDataStructures/stack.c)

## 🧠 Notes & Insights

* Think of it like a **stack of plates** — you can only touch the top one.
* Excellent model for recursion and backtracking algorithms.
* In C, stack overflow happens when recursion depth exceeds allocated memory.
* Conceptually simple but forms the backbone of **compilers, interpreters, and VMs**.
