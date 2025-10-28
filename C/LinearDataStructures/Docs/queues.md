# Circular Queue

**Purpose**: Fixed-size FIFO buffer with O(1) enqueue/dequeue operations  
**Core Idea**: Circular array with head and tail pointers that wrap around  

**Structure**:

```pseudo
Queue:
  - arr: array[capacity]
  - head: integer (index)
  - tail: integer (index) 
  - capacity: integer
  - size: integer
```

**Key Operations**:

- `enqueue()`: O(1)
- `dequeue()`: O(1)
- `is_empty()`: O(1)
- `is_full()`: O(1)

**Pointer Movement**:

```pseudo
Normal Array:
  tail = tail + 1

Circular Buffer:
  tail = (tail + 1) % capacity
  head = (head + 1) % capacity
```

**Memory**: Fixed array of size N + 5 integers (head, tail, capacity, size)  
**Use When**: Fixed-size buffers, producer-consumer patterns, sliding window algorithms

---

## Quick Notes

- **Structure**: Array + Head index + Tail index + Capacity + Size
- **Circular Nature**: Modulo arithmetic for wrap-around
- **Full Condition**: size == capacity
- **Empty Condition**: size == 0
- **Trade-off**: Fixed size vs O(1) operations
- **Good for**: Fixed buffers, embedded systems, performance-critical code
- **Bad for**: Dynamic resizing needs

---

## Key Implementation Details

- **Wrap-around**: `index = (index + 1) % capacity`
- **Head/Tail**: Head points to next element to dequeue, Tail to next empty slot
- **No Shifting**: Elements stay in place, only pointers move
- **Memory**: Pre-allocated array, no runtime allocations
