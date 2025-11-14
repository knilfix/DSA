
# 🌳 DSA Mastery Road map — Phase 1 (11 Weeks)

> Goal: Master core Trees & Graphs for strong problem-solving skills and future systems projects.

---

## 📅 Week 1-2: Binary Trees & BST Fundamentals

### ✅ Week 1: Binary Tree Basics

**Theory:**

- Tree terminology (root, leaf, height, depth)
- Traversals: Pre-order, In-order, Post-order, Level-order
- Types: Complete, Full, Perfect

**Implementation Checklist (C):**

```c
typedef struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode* create_node(int data);
void preorder(TreeNode* root);
void inorder(TreeNode* root);
void postorder(TreeNode* root);
void level_order(TreeNode* root);
int tree_height(TreeNode* root);
int count_nodes(TreeNode* root);
int count_leaves(TreeNode* root);
void destroy_tree(TreeNode* root);
````

**Practice:**

- Find max element
- Check if balanced
- Print root-to-leaf paths
- Diameter of tree
- Mirror binary tree

---

### ✅ Week 2: Binary Search Trees (BST)

**Theory:**

- BST property: left < root < right
- Time complexity: average O(log n), worst O(n)

**Implementation Checklist (C):**

```c
TreeNode* insert(TreeNode* root, int data);
TreeNode* search(TreeNode* root, int target);
TreeNode* find_min(TreeNode* root);
TreeNode* find_max(TreeNode* root);
TreeNode* delete_node(TreeNode* root, int data);
bool is_valid_bst(TreeNode* root);
TreeNode* find_successor(TreeNode* root, int data);
TreeNode* find_predecessor(TreeNode* root, int data);
```

**Practice:**

- kth smallest
- sorted array → BST
- check identical BSTs
- LCA in BST
- range sum query

---

## 📅 Week 3-4: Red-Black Trees (Self-balancing)

### ✅ Week 3: RB Tree Basics

**Theory:**

- Node colors: Red / Black
- Properties ensuring balance
- Rotations: Left, Right
- Fix-ups after insert

**Implementation Checklist (C):**

```c
typedef enum { RED, BLACK } Color;

typedef struct RBNode {
    int data;
    Color color;
    struct RBNode *left, *right, *parent;
} RBNode;

RBNode* insert(RBNode* root, int data);
void rotate_left(RBNode** root, RBNode* x);
void rotate_right(RBNode** root, RBNode* y);
void fix_insert(RBNode** root, RBNode* z);
```

**Practice:**

- color violations handling
- prove height O(log n)

---

### ✅ Week 4: RB Tree Delete + Analysis

**Focus:**

- deletion fix-ups
- RB vs BST performance
- height measurement tests

**Tasks:**

- complete delete operation
- stress test 10k inserts
- compare: skewed BST vs RB Tree

---

## 📅 Week 5-6: Graph Fundamentals

### ✅ Week 5: Graph Reps

**Theory:**

- Directed/Undirected
- Weighted/Unweighted
- Adjacency Matrix vs List

**Implementation Checklist (C):**

```c
typedef struct Node {
    int vertex;
    int weight;
    struct Node* next;
} Node;

typedef struct Graph {
    int num_vertices;
    Node** adj_list;
} Graph;

Graph* create_graph(int vertices);
void add_edge(Graph* g, int src, int dest, int weight);
void print_graph(Graph* g);
void destroy_graph(Graph* g);
```

**Practice:**

- convert matrix ↔ list
- degree counting
- self-loop detection
- neighbors of vertex

---

### ✅ Week 6: BFS & DFS Traversal

**Theory:**

- BFS uses queue
- DFS uses stack/recursion
- Complexity: O(V + E)

**Implementation Checklist (C):**

```c
void dfs_recursive(Graph* g, int vertex, bool* visited);
void dfs_iterative(Graph* g, int start);
void bfs(Graph* g, int start);
bool is_connected(Graph* g);
bool has_cycle_undirected(Graph* g);
bool has_cycle_directed(Graph* g);
void print_all_paths(Graph* g, int src, int dest);
```

**Practice:**

- connected components
- unweighted shortest path (BFS)
- bipartite checking

---

## 📅 Week 7-9: Graph Algorithms

### ✅ Week 7: Shortest Paths

**Theory:**

- Dijkstra (no negative weights)
- Bellman-Ford (negative OK)
- PQ optimization via heap

**Implementation Checklist (C):**

```c
int* dijkstra(Graph* g, int source);
int* bellman_ford(Graph* g, int source);
bool has_negative_cycle(Graph* g);
void print_shortest_paths(Graph* g, int source);
```

---

### ✅ Week 8: Minimum Spanning Trees

**Theory:**

- Kruskal + Union-Find
- Prim + PQ

**Implementation Checklist (C):**

```c
typedef struct { int src, dest, weight; } Edge;

typedef struct {
    int* parent;
    int* rank;
} UnionFind;

UnionFind* create_uf(int n);
int find(UnionFind* uf, int x);
void union_sets(UnionFind* uf, int x, int y);

Edge* kruskal_mst(Graph* g, int* num_edges);
Edge* prim_mst(Graph* g, int* num_edges);
```

---

### ✅ Week 9: Topological Sort

**Theory:**

- DAG requirement
- Kahn’s BFS method
- DFS ordering

**Implementation Checklist (C):**

```c
int* topological_sort_kahn(Graph* g);
int* topological_sort_dfs(Graph* g);
bool is_dag(Graph* g);
```

---

## 📅 Week 10-11: Integration Topics

### ✅ Week 10: Heaps

**Theory:**

- min/max heap properties
- array indexing tricks

**Implementation Checklist (C):**

```c
typedef struct {
    int* arr;
    int size;
    int capacity;
} MinHeap;

MinHeap* create_heap(int capacity);
void insert(MinHeap* h, int data);
int extract_min(MinHeap* h);
void heapify_down(MinHeap* h, int idx);
void heapify_up(MinHeap* h, int idx);
int peek(MinHeap* h);
```

---

### ✅ Week 11: Tries

**Theory:**

- prefix search O(m)
- space usage tradeoffs

**Implementation Checklist (C):**

```c
typedef struct TrieNode {
    struct TrieNode* children[26];
    bool is_end_of_word;
} TrieNode;

TrieNode* create_trie();
void insert_word(TrieNode* root, char* word);
bool search(TrieNode* root, char* word);
bool starts_with(TrieNode* root, char* prefix);
void delete_word(TrieNode* root, char* word);
```

---

## ✅ Success Metrics Before Phase 2

- Implement BST + RB Tree from memory
- DFS/BFS without reference
- Dijkstra explanation solid
- MST using both algorithms
- Heap operations correct
- Graph + tree problems solved 50+
- Code clean + in GitHub
- Personal DSA notes complete

---

## 🧩 Daily Plan

**Weekdays (3 hours):**

- 30m review
- 90m coding
- 60m problems

**Weekends (5 hours):**

- Saturday: catch up + challenges
- Sunday: review and plan

---

> Consistency wins. Slow is smooth. Smooth is fast.

```

---

If you want, I can also create:

✅ a separate `DSA_Projects.md` with projects directly mapped to each week  
✅ a folder structure layout you can initialize on your machine  
✅ tiny badges you can tick off for each data structure you master  

Anything else you want tweaked before you toss this into GitHub?
```

## 🎯 **Weekly Success Metrics**

Each week, you should be able to:

1. ✅ Implement the data structure from scratch in C
2. ✅ Explain time/space complexity
3. ✅ Solve 3-5 related problems
4. ✅ Connect to real-world application
5. ✅ Add to your notes/cheatsheet

---

## 📚 **Learning Resources**

**Books:**

- "Introduction to Algorithms" (CLRS) - Reference
- "Grokking Algorithms" - Visual explanations

**Online:**

- VisuAlgo.net - Visualize algorithms
- LeetCode - Problems (Easy → Medium focus)
- GeeksforGeeks - Detailed explanations
- Your own implementations on GitHub!

**YouTube Channels:**

- Abdul Bari (algorithms)
- WilliamFiset (graph algorithms)
- MIT OpenCourseWare (6.006)

---

## 🔗 **Bridge to Phase 2 Projects**

### **HTTP Server (Month 4)**

**DSA Applications:**

- Hash table → Routing table (`GET /api/users → handler`)
- Trie → Fast URL matching
- Queue → Connection pool

### **Messaging App (Months 5-6)**

**DSA Applications:**

- Graph → User/room relationships
- Queue → Message buffering
- Heap → Priority messages

### **Database (Months 7-9)**

**DSA Applications:**

- BST/AVL → Primary key index
- Hash table → Quick lookups
- B-Tree → Disk-based storage (research this!)

---

## 🎓 **Phase 1 Completion Checklist**

Before moving to Phase 2, ensure you can:

- [ ] Implement BST, AVL from memory
- [ ] Code DFS/BFS without reference
- [ ] Explain Dijkstra's algorithm clearly
- [ ] Build MST using Kruskal's/Prim's
- [ ] Implement min-heap operations
- [ ] Solve 50+ LeetCode problems (20 Easy, 25 Medium, 5 Hard)
- [ ] Have clean, documented code in your GitHub repo
- [ ] Write your own DSA cheatsheet/notes

---

## 💪 **Your Daily Routine**

**Weekdays (3 hours):**

- 08:00-08:30: Review yesterday's work
- 08:30-10:00: New implementation
- 10:00-11:00: Problem solving

**Weekends (5 hours):**

- Saturday: Catch up + harder problems
- Sunday: Review week + prepare next week

**Tips:**

1. Code everything by hand first (on paper)
2. Use debugger to understand pointer operations
3. Draw diagrams for every algorithm
4. Explain concepts to rubber duck/friend
5. Commit daily to GitHub (green squares!)

---

## 🚀 **Ready to Start?**

**Week 1 begins Monday. Your first task:**

1. Create `/DSA/Trees/BinaryTree/` directory
2. Implement `create_node()` and basic tree structure
3. Write preorder traversal (recursive)
4. Test with a simple tree

**Remember:** Slow is smooth, smooth is fast. Master each concept before moving forward.

You've got this! 🌳💻
