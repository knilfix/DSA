
# ⚙️ DSA LAB  
>
> *A structured journey from Arrays to Algorithms*  
Maintainer: **Mark** | Started: *Year 1* | Phase: *Trees & Beyond 🌳*
> *"Don't just implement data structures — understand the invariants that make them work."*

---

## 🎯 Current Sprint (Active Focus)

**This Week:**

- [ ] Fix Red-Black Tree deletion bug (if parent is NIL check)
- [ ] Test RB-Tree with 100+ sequential insertions
- [ ] Write notes on B-Tree splitting logic (concept exposure)

**This Month:**

- [ ] Complete RB-Tree deletion implementation
- [ ] Implement basic B-Tree insertion
- [ ] Start graph representation (adjacency list)

---

## ✅ Stage 1: Linear Foundations (MASTERED)

**Core Structures**

- [x] Arrays (dynamic resizing, O(1) access)
- [x] Linked Lists (singly, doubly, circular) - *Implemented in C*
- [x] Stacks (LIFO, function call simulation) - *Implemented in C*
- [x] Queues (FIFO, circular buffer) - *Implemented in C*
- [x] Hash Tables (chaining, rehashing, load factor) - *Dart implementation*

**Key Concepts Mastered**

- [x] Pointer manipulation & memory management
- [x] O(1) vs O(n) operations (tail pointer optimization)
- [x] Dynamic resizing strategies
- [x] Collision resolution (separate chaining)

**Milestone Projects**

- [x] HashMap with linked list chaining (Dart)
- [x] Circular queue implementation (C)
- [x] Campus navigation system (Graph + Dijkstra in Dart)

**Confidence:** 9/10 - *Can implement from memory, understand trade-offs*

---

## 🌳 Stage 2: Tree Structures (IN PROGRESS)

### Binary Search Trees ✅

- [x] Insert operation
- [x] Delete operation (3 cases: leaf, one child, two children)
- [x] Traversals (in-order, pre-order, post-order, level-order)
- [x] Search operation
- [x] Understand BST invariant: `left < parent < right`

**Confidence:** 8/10

---

### Red-Black Trees ⚙️

**Completed:**

- [x] Understand 5 RB properties
- [x] Insert operation
- [x] Fix-up after insertion (recoloring + rotations)
- [x] Left rotation
- [x] Right rotation
- [x] Handle NIL sentinel nodes
- [x] Fix parent pointer bug (root.parent = NIL)
- [x] Test with sequential insertions (0-10)

**In Progress:**

- [ ] Delete operation
- [ ] Fix-up after deletion
- [ ] Verify all 5 properties hold after operations

**To Practice:**

- [ ] Rebuild from memory (no reference)
- [ ] Test with 1000+ nodes
- [ ] Visualize color changes during insertion

**Confidence:** 6/10 - *Insertion solid, deletion next*

---

### B-Trees 🚧

**Concept Phase (Exposure):**

- [ ] Understand multi-key nodes structure
- [ ] Learn node splitting logic (when node is full)
- [ ] Understand why all leaves stay at same depth
- [ ] Learn insertion algorithm
- [ ] Learn deletion algorithm (merging/redistribution)

**Implementation Phase:**

- [ ] Create B-Tree node structure (order m)
- [ ] Implement search
- [ ] Implement insert with splitting
- [ ] Implement delete with merging
- [ ] Test with varying orders (m=3, m=5, m=7)

**Applications to Learn:**

- [ ] Why databases use B+ Trees
- [ ] Disk block efficiency
- [ ] Range queries optimization

**Confidence:** 0/10 - *Not started*

---

### Other Trees (Optional/Future)

- [ ] AVL Trees (height-balanced alternative to RB)
- [ ] B+ Trees (leaf-linked for range queries)
- [ ] Trie (prefix trees for strings)
- [ ] Segment Trees (range queries)

---

## 🌐 Stage 3: Graphs

### Graph Representations

- [ ] Adjacency List (most common)
- [ ] Adjacency Matrix (dense graphs)
- [ ] Edge List (simple representation)
- [ ] Understand space/time trade-offs

### Traversals

- [ ] Depth-First Search (DFS) - uses stack
- [ ] Breadth-First Search (BFS) - uses queue
- [ ] Understand recursive vs iterative DFS
- [ ] Practice on different graph types (directed, undirected, weighted)

### Shortest Path Algorithms

- [x] Dijkstra's Algorithm - *Used in campus navigation*
- [ ] Bellman-Ford (handles negative weights)
- [ ] Floyd-Warshall (all-pairs shortest path)
- [ ] A* (heuristic-based)

### Advanced Graph Algorithms

- [ ] Topological Sort (DAG ordering)
- [ ] Cycle Detection (DFS-based)
- [ ] Union-Find / Disjoint Set
- [ ] Minimum Spanning Tree (Kruskal's, Prim's)
- [ ] Strongly Connected Components (Tarjan's)

**Milestone Project Ideas:**

- [ ] Pathfinder visualizer (BFS/Dijkstra animation)
- [ ] Social network graph (connections, mutual friends)
- [ ] Dependency resolver (topological sort)

**Confidence:** 2/10 - *Basic Dijkstra done, need formal study*

---

## ⚙️ Stage 4: Systems-Level Integration

**Goal:** Combine DSAs to solve real problems

### Projects to Build

- [ ] LRU Cache (HashMap + Doubly Linked List)
- [ ] Priority Queue (Heap implementation)
- [ ] Job Scheduler (Heap + Queue)
- [ ] Autocomplete Engine (Trie + HashMap)
- [ ] Symbol Table (BST/RB-Tree + HashMap)
- [ ] Mini Database Index (B+ Tree simulation)

### Skills to Develop

- [ ] Choose right DSA for the problem
- [ ] Analyze space/time trade-offs
- [ ] Design clean APIs (like GraphManager)
- [ ] Handle edge cases and errors
- [ ] Write comprehensive tests

**Confidence:** 3/10 - *Campus nav shows capability, need more practice*

---

## 🧮 Stage 5: Core Algorithms

### Sorting

- [ ] Merge Sort (O(n log n), stable)
- [ ] Quick Sort (O(n log n) average, in-place)
- [ ] Heap Sort (O(n log n), in-place)
- [ ] Counting Sort (O(n+k), non-comparison)
- [ ] Radix Sort (O(d*n), for integers)

### Searching

- [ ] Binary Search (iterative)
- [ ] Binary Search (recursive)
- [ ] Binary Search variations (first/last occurrence)

### Dynamic Programming

- [ ] Fibonacci (memoization vs tabulation)
- [ ] Knapsack Problem
- [ ] Longest Common Subsequence
- [ ] Coin Change Problem
- [ ] Matrix Chain Multiplication

### Greedy Algorithms

- [ ] Activity Selection
- [ ] Huffman Encoding
- [ ] Fractional Knapsack

**Confidence:** 4/10 - *Understand basics, need practice*

---

## 🔁 Stage 6: Mastery Through Repetition

### Rebuild Without Reference

- [ ] Stack (C)
- [ ] Queue (C)
- [ ] Linked List (C)
- [ ] HashMap (any language)
- [ ] BST (any language)
- [ ] Red-Black Tree (C or Python)
- [ ] Graph (adjacency list)

### Language Diversification

- [x] C - Linear structures
- [x] Dart - HashMap, Graph
- [x] Python - Red-Black Tree
- [ ] Rust/Go - (future learning)

### Optimization Practice

- [ ] Reduce RB-Tree rotate calls
- [ ] Optimize graph traversal memory
- [ ] Profile and benchmark implementations

---

## 📊 Progress Metrics

| Category       | Structures Known | Confidence | Last Worked On |
| -------------- | ---------------- | ---------- | -------------- |
| Linear DSA     | 5/5              | 9/10       | Completed      |
| Basic Trees    | 1/1 (BST)        | 8/10       | Completed      |
| Balanced Trees | 1/2 (RB done)    | 6/10       | This week      |
| Advanced Trees | 0/3              | 0/10       | Not started    |
| Graphs         | 1/8              | 2/10       | Used Dijkstra  |
| Algorithms     | 2/15             | 4/10       | Ongoing        |

---

## 🎓 Learning Philosophy

**What's Working:**

- ✅ C foundation gave deep memory/pointer understanding
- ✅ "Exposure → Understanding → Implementation" approach
- ✅ Focus on invariants, not just code
- ✅ Building real projects (campus navigation)
- ✅ Understanding "why" structures exist

**Key Insights:**
> *"A tree without rules is just a tree. But `left < parent < right` makes it a BST - quick by design."*

> *"Sometimes the best way to tackle a problem is not to code but to design a structure that solves it by itself."*

> *"Smart structures beat clever code. Tail pointer = O(1) append instead of O(n) loop."*

---

## 📅 Revision Schedule

**Weekly:**

- [ ] Review one completed structure (rebuild or explain)
- [ ] Solve 2-3 LeetCode problems using current focus area

**Monthly:**

- [ ] Major milestone check (complete one structure)
- [ ] Update this roadmap with confidence levels
- [ ] Write summary of what was learned

**Quarterly:**

- [ ] Rebuild all linear structures from memory
- [ ] Complete one systems-level project
- [ ] Assess readiness for next phase

---

## 🏆 Milestones & Checkpoints

### Completed ✅

- [x] Master pointer manipulation in C
- [x] Implement all linear structures
- [x] Build production-quality HashMap
- [x] Understand BST operations fully
- [x] Implement RB-Tree insertion
- [x] Apply DSA to real project (campus nav)

### Current Goals 🎯

- [ ] Complete Red-Black Tree (insertion + deletion)
- [ ] Understand B-Tree concepts deeply
- [ ] Start graph algorithm implementations

### Future Milestones 🚀

- [ ] Implement all common graph algorithms
- [ ] Build 3+ systems-level integration projects
- [ ] Competitive programming readiness
- [ ] Interview-level DSA fluency

---

**Last Updated:** October 2025  
**Next Review:** When RB-Tree deletion is complete
