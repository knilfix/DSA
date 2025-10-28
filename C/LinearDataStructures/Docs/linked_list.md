# Linked List

**Purpose**: Dynamic data structure with efficient insertions/deletions at both ends  
**Core Idea**: Nodes with data + pointer to next node, maintaining head and tail pointers  
**Key Operations**:

- `append()`: O(1) (with tail pointer)
- `prepend()`: O(1)
- `insert_after()`: O(n) search + O(1) insertion
- `delete_front()`: O(1)
- `delete_end()`: O(n) (singly-linked) or O(1) (doubly-linked)
- `delete_at_value()`: O(n) search + O(1) deletion
- `reverse()`: O(n)

**Memory**: N nodes × (data + pointer)  
**Use When**: Frequent insertions/deletions, unknown size, stack/queue operations

---

## Quick Notes

- **Structure**:

```pseudo
- STRUCT Node
    data: integer
    next: pointer to Node

STRUCT LinkedList
    head: pointer to Node
    tail: pointer to Node  
    size: integer

```

- **Tail Optimization**: O(1) appends
- **Edge Cases**: Empty list, single node, head/tail updates
- **Trade-off**: O(1) insert/delete vs O(n) random access
- **Good for**: Stacks, queues, dynamic data
- **Bad for**: Random access, binary search

---

## Key Implementation Details

- **Memory Management**: Manual allocation/free for each node
- **Empty List**: Head = Tail = NULL, Size = 0
- **Single Node**: Head = Tail = same node
- **Reverse**: Three-pointer technique (prev, current, next)
- **Deletion**: Always update tail if deleting last node
