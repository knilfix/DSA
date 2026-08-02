# Queue Practice Exercises

## Basic Operations

### 1. QueueUsingStacks

Implement a queue using only stack operations (LIFO structure).

**Methods to implement:**

- `enqueue(x)` - Add element to back of queue
- `dequeue()` - Remove and return front element
- `peek()` - Get the front element
- `empty()` - Return whether queue is empty

**Challenge:** Make either enqueue or dequeue amortized O(1) time

**Skills tested:** Data structure conversion, amortized analysis

---

### 2. CircularQueueImplementation

Design a circular queue that uses a fixed-size array efficiently.

**Methods to implement:**

- `enqueue(value)` - Insert element, return true if successful
- `dequeue()` - Delete element, return true if successful
- `front()` - Get front item
- `rear()` - Get last item
- `isEmpty()` - Check if queue is empty
- `isFull()` - Check if queue is full

**Example:**

```t
queue = CircularQueue(3)
queue.enqueue(1)  # True
queue.enqueue(2)  # True
queue.enqueue(3)  # True
queue.enqueue(4)  # False (full)
queue.rear()      # 3
queue.isFull()    # True
queue.dequeue()   # True
queue.enqueue(4)  # True
queue.rear()      # 4
```

**Skills tested:** Circular buffer, modular arithmetic, space efficiency

---

## Classic Queue Problems

### 3. GenerateBinaryNumbers

Generate binary numbers from 1 to N using a queue.

**Function Signature:** `def generateBinary(n: int) -> List[str]`

**Example:**

- Input: `n = 5`
- Output: `["1", "10", "11", "100", "101"]`

**Skills tested:** Queue-based generation, binary patterns

---

### 4. FirstNonRepeatingCharacter

Given a stream of characters, find the first non-repeating character at each point.

**Function Signature:** `def firstNonRepeating(stream: str) -> List[str]`

**Example:**

- Input: `"aabccxb"`
- Output: `["a", "a", "#", "b", "b", "b", "x"]`
  - `#` means no non-repeating character

**Skills tested:** Queue + HashMap, streaming data

---

### 5. SlidingWindowMaximum

Given an array and a window size k, find the maximum in each sliding window.

**Function Signature:** `def maxSlidingWindow(nums: List[int], k: int) -> List[int]`

**Example:**

- Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- Output: `[3,3,5,5,6,7]`
- Windows: `[1 3 -1]`, `[3 -1 -3]`, `[-1 -3 5]`, etc.

**Skills tested:** Deque, monotonic queue pattern

---

### 6. TimeBasedKeyValueStore

Design a time-based key-value store that can store multiple values for the same key at different timestamps and retrieve the value at a certain timestamp.

**Methods to implement:**

- `set(key, value, timestamp)` - Store key-value pair at timestamp
- `get(key, timestamp)` - Get value at given timestamp (or most recent before it)

**Example:**

```t
store = TimeMap()
store.set("foo", "bar", 1)
store.get("foo", 1)  # returns "bar"
store.get("foo", 3)  # returns "bar"
store.set("foo", "bar2", 4)
store.get("foo", 4)  # returns "bar2"
store.get("foo", 5)  # returns "bar2"
```

**Skills tested:** Timestamp ordering, binary search with queue concepts

---

## BFS & Level Order Problems

### 7. BinaryTreeLevelOrder

Given a binary tree, return the level order traversal of its nodes' values (left to right, level by level).

**Function Signature:** `def levelOrder(root: TreeNode) -> List[List[int]]`

**Example:**

```t
Input tree:
    3
   / \
  9  20
    /  \
   15   7

Output: [[3], [9,20], [15,7]]
```

**Skills tested:** BFS, queue for tree traversal

---

### 8. BinaryTreeRightSideView

Given a binary tree, return the values of nodes you can see when looking from the right side.

**Function Signature:** `def rightSideView(root: TreeNode) -> List[int]`

**Example:**

```t
Input tree:
    1
   / \
  2   3
   \   \
    5   4

Output: [1, 3, 4]
```

**Skills tested:** Level-order traversal, tracking last element

---

### 9. BinaryTreeZigzagLevelOrder

Return the zigzag level order traversal (left to right, then right to left alternating).

**Function Signature:** `def zigzagLevelOrder(root: TreeNode) -> List[List[int]]`

**Example:**

```t
Input tree:
    3
   / \
  9  20
    /  \
   15   7

Output: [[3], [20,9], [15,7]]
```

**Skills tested:** Deque, direction alternation

---

## Advanced Queue Problems

### 10. ShortestPathInBinaryMatrix

Given an n x n binary matrix (0 = walkable, 1 = blocked), find the shortest path from top-left to bottom-right. You can move in 8 directions.

**Function Signature:** `def shortestPath(grid: List[List[int]]) -> int`

**Example:**

```t
Input:
[[0,1],
 [1,0]]
Output: 2

Input:
[[0,0,0],
 [1,1,0],
 [1,1,0]]
Output: 4
```

**Skills tested:** BFS for shortest path, grid traversal

---

### 11. SnakesAndLadders

Given a board game with snakes and ladders, find the minimum number of dice rolls to reach the end.

**Function Signature:** `def snakesAndLadders(board: List[List[int]]) -> int`

**Example:**

- Board size: 6x6
- Find minimum moves from square 1 to square 36
- Return -1 if impossible

**Skills tested:** BFS on graph, game simulation

---

### 12. OpenTheLock

You have a lock with 4 circular wheels (each 0-9). Given a target combination and a list of "dead ends" you cannot use, find minimum turns needed to reach target from "0000".

**Function Signature:** `def openLock(deadends: List[str], target: str) -> int`

**Example:**

- `deadends = ["0201","0101","0102","1212","2002"]`
- `target = "0202"`
- Output: `6`

**Skills tested:** BFS, state space exploration

---

## Design Problems

### 13. DesignHitCounter

Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).

**Methods to implement:**

- `hit(timestamp)` - Record a hit at given timestamp
- `getHits(timestamp)` - Return hits in past 5 minutes

**Example:**

```t
counter = HitCounter()
counter.hit(1)
counter.hit(2)
counter.hit(3)
counter.getHits(4)    # returns 3
counter.hit(300)
counter.getHits(300)  # returns 4
counter.getHits(301)  # returns 3
```

**Skills tested:** Queue with time-based expiry, sliding window

---

### 14. MovingAverage

Design a class to find the moving average from a data stream within a sliding window.

**Methods to implement:**

- `MovingAverage(size)` - Initialize with window size
- `next(val)` - Add value and return current moving average

**Example:**

```t
ma = MovingAverage(3)
ma.next(1)  # returns 1.0
ma.next(10) # returns 5.5
ma.next(3)  # returns 4.67
ma.next(5)  # returns 6.0 (window is now [10,3,5])
```

**Skills tested:** Circular queue, running calculations

---

## Multi-Queue Problems

### 15. TaskScheduler

Given tasks represented by characters and a cooldown period n, find the minimum time to complete all tasks. Same task must wait n intervals before running again.

**Function Signature:** `def leastInterval(tasks: List[str], n: int) -> int`

**Example:**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`
- Explanation: `A -> B -> idle -> A -> B -> idle -> A -> B`

**Skills tested:** Priority queue + regular queue, scheduling

---

### 16. NumberOfRecentCalls

Design a class that counts recent requests within a 3000ms time window.

**Methods to implement:**

- `ping(t)` - Add new request at time t, return count of requests in [t-3000, t]

**Example:**

```t
counter = RecentCounter()
counter.ping(1)     # returns 1
counter.ping(100)   # returns 2
counter.ping(3001)  # returns 3
counter.ping(3002)  # returns 3 (request at t=1 expired)
```

**Skills tested:** Queue with expiry, time window management

---

## Tips for Practice

1. **Think FIFO:** First In, First Out - process in order received
2. **BFS Master Pattern:** Queue is essential for breadth-first search
3. **Deque Power:** Double-ended queue gives you flexibility
4. **Time Windows:** Queue naturally handles time-based expiry
5. **Level Processing:** Use queue size to process levels in trees/graphs

## Common Queue Patterns

- **Level-Order Traversal:** BFS in trees and graphs
- **Sliding Window:** Fixed or variable size windows
- **State Exploration:** BFS for shortest path problems
- **Task Scheduling:** Managing order of execution
- **Stream Processing:** Handling continuous data flow
- **Time-Based Expiry:** Maintaining recent data within time windows
