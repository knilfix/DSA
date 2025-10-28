# Stack

**Purpose**: LIFO (Last-In-First-Out) dynamic data structure  
**Core Idea**: Array-based stack with automatic resizing  

**Structure**:

```pseudo
Stack:
  - arr: array of integers
  - size: integer (current elements)
  - capacity: integer (max capacity)
```

**Key Operations**:

- `push()`: O(1) amortized
- `pop()`: O(1)
- `peek()`: O(1) - view top element

**Pointer Movement**:

```pseudo
Push: arr[size] = data, then size++
Pop:  data = arr[size-1], then size--
```

**Memory**: Dynamic array that doubles when full  
**Use When**: LIFO operations, recursion, undo/redo, DFS

---

## Quick Notes

- **Resizing Strategy**: Double capacity when full
- **Top Element**: Always at `arr[size-1]`
- **Empty Condition**: size == 0
- **Full Condition**: size == capacity
- **Trade-off**: Amortized O(1) vs occasional resize cost
- **Good for**: Function calls, expression evaluation, backtracking
- **Bad for**: Random access, FIFO operations

---

## Key Implementation Details

- **Resize**: Allocate new array, copy elements, free old array
- **No Shrink**: Capacity doesn't reduce on pop (simplicity)
- **Top Access**: Direct access via `size-1` index
- **Memory**: Dynamic allocation with manual management

Clean and consistent! 📓✨
