# Graphs

## 🧩 **Definition**

A **Graph** is a non-linear data structure consisting of **nodes (vertices)** and **edges** that connect pairs of nodes.
Graphs are used to model **relationships** or **connections** between entities.

---

## 💡 **Core Idea**

Graphs exist to represent **networks** — situations where elements connect to multiple others, not just in a parent–child hierarchy.
They’re essential when relationships are **many-to-many**, like roads between cities, friendships between users, or links between web pages.

---

## ⚙️ **Key Operations**

| Operation           | Description                | Time Complexity       |
| ------------------- | -------------------------- | --------------------- |
| `add_vertex(v)`     | Adds a vertex to the graph | O(1)                  |
| `add_edge(u, v)`    | Connects vertex u to v     | O(1) (adjacency list) |
| `remove_edge(u, v)` | Removes an edge            | O(1)–O(V)             |
| `search(v)`         | Check if a vertex exists   | O(1)                  |
| `bfs(start)`        | Breadth-first traversal    | O(V + E)              |
| `dfs(start)`        | Depth-first traversal      | O(V + E)              |

---

## 🧱 **Internal Concept**

Graphs are typically represented in two common ways:

### **1. Adjacency List (Most Common)**

Each vertex stores a list of adjacent vertices — usually implemented with a **dictionary of lists** or a **linked list array**.

```t
A → [B, C]
B → [A, D]
C → [A, D]
D → [B, C]
```

Efficient for **sparse graphs** (few edges relative to vertices).

### **2. Adjacency Matrix**

A 2D array where each cell `(i, j)` is `1` if there’s an edge between vertex `i` and vertex `j`, otherwise `0`.

```t
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 1 ]
D [ 0 1 1 0 ]
```

Efficient for **dense graphs** but takes more space: O(V²).

---

## 🧭 **Use Cases**

* **Social networks** (friend connections)
* **Maps / Navigation** (roads, routes)
* **Recommendation systems** (related items)
* **Search engines** (link graph of the web)
* **Scheduling** and **dependency resolution** (DAGs)

---

## 🧮 **Complexity Overview**

| Operation   | Adjacency List | Adjacency Matrix |
| ----------- | -------------- | ---------------- |
| Space       | O(V + E)       | O(V²)            |
| Add Vertex  | O(1)           | O(V²)            |
| Add Edge    | O(1)           | O(1)             |
| Remove Edge | O(E)           | O(1)             |
| BFS / DFS   | O(V + E)       | O(V²)            |

---

## 🧰 **Implementation References**

* **Python:** [../Python/playground/bst.py](../Python/playground/bst.py) *(or create `graphs.py`)*
* **C:** [../C/NonLinearDataStructures/Graphs/graphs.c](../C/NonLinearDataStructures/Graphs/graphs.c)

---

## 🧠 **Notes & Insights**

* Graphs can be **directed** or **undirected**.
* Edges can be **weighted** (for costs/distances).
* Many real-world problems boil down to **graph traversal** (BFS, DFS).
* The data structure choice (list vs matrix) depends on **sparsity** and **operation frequency**.
* Many advanced algorithms (Dijkstra, Bellman-Ford, Kruskal, etc.) are built on top of these basic structures.

---
