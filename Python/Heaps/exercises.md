# Heap Practice Exercises

## Basic Heap Operations

### 1. KthLargestElement

Find the kth largest element in an unsorted array.

**Function Signature:** `def findKthLargest(nums: List[int], k: int) -> int`

**Example:**

- Input: `nums = [3,2,1,5,6,4]`, `k = 2`
- Output: `5`

**Skills tested:** Min heap of size k, heap property understanding

---

### 2. KthSmallestElement

Find the kth smallest element in an unsorted array.

**Function Signature:** `def findKthSmallest(nums: List[int], k: int) -> int`

**Example:**

- Input: `nums = [7,10,4,3,20,15]`, `k = 3`
- Output: `7`

**Skills tested:** Max heap of size k, inverse thinking

---

### 3. LastStoneWeight

You have stones with given weights. Each turn, take two heaviest stones and smash them. If weights differ, the stone becomes the difference. Return the weight of the last remaining stone (or 0).

**Function Signature:** `def lastStoneWeight(stones: List[int]) -> int`

**Example:**

- Input: `[2,7,4,1,8,1]`
- Process: `8,7 → 1`, then `4,2 → 2`, etc.
- Output: `1`

**Skills tested:** Max heap operations, simulation

---

## Top-K Problems

### 4. TopKFrequentElements

Given an array and integer k, return the k most frequent elements.

**Function Signature:** `def topKFrequent(nums: List[int], k: int) -> List[int]`

**Example:**

- Input: `nums = [1,1,1,2,2,3]`, `k = 2`
- Output: `[1,2]`

**Skills tested:** Frequency map + heap, bucket sort alternative

---

### 5. TopKFrequentWords

Given a list of words and k, return the k most frequent words. If tied, return in lexicographic order.

**Function Signature:** `def topKFrequent(words: List[str], k: int) -> List[str]`

**Example:**

- Input: `words = ["i","love","leetcode","i","love","coding"]`, `k = 2`
- Output: `["i","love"]`

**Skills tested:** Custom comparator with heap, frequency + lexicographic ordering

---

### 6. KClosestPointsToOrigin

Find the k closest points to origin (0, 0) on a 2D plane.

**Function Signature:** `def kClosest(points: List[List[int]], k: int) -> List[List[int]]`

**Example:**

- Input: `points = [[1,3],[-2,2]]`, `k = 1`
- Output: `[[-2,2]]` (distance = √8 < √10)

**Skills tested:** Max heap with custom distance, coordinate geometry

---

## Merge Problems

### 7. MergeKSortedLists

Merge k sorted linked lists into one sorted list.

**Function Signature:** `def mergeKLists(lists: List[ListNode]) -> ListNode`

**Example:**

- Input: `[[1,4,5], [1,3,4], [2,6]]`
- Output: `[1,1,2,3,4,4,5,6]`

**Skills tested:** Min heap with k elements, efficient merging

---

### 8. KthSmallestInSortedMatrix

Given an n x n matrix where each row and column is sorted, find the kth smallest element.

**Function Signature:** `def kthSmallest(matrix: List[List[int]], k: int) -> int`

**Example:**

```t
matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
Output: 13
```

**Skills tested:** Min heap for matrix traversal, multi-way merge

---

### 9. FindMedianFromDataStream

Design a data structure that supports adding numbers and finding the median.

**Methods to implement:**

- `addNum(num)` - Add a number to the data structure
- `findMedian()` - Return the median of all elements

**Example:**

```t
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.findMedian()  # returns 1.5
medianFinder.addNum(3)
medianFinder.findMedian()  # returns 2.0
```

**Skills tested:** Two heaps (max heap + min heap), balancing

---

## Scheduling & Intervals

### 10. MeetingRoomsII

Given an array of meeting time intervals, find the minimum number of conference rooms required.

**Function Signature:** `def minMeetingRooms(intervals: List[List[int]]) -> int`

**Example:**

- Input: `[[0,30], [5,10], [15,20]]`
- Output: `2` (one room for [0,30], another for [5,10] and [15,20])

**Skills tested:** Min heap for tracking end times, greedy scheduling

---

### 11. TaskScheduler

Given tasks and a cooldown period n, find the minimum time to complete all tasks. Same task must wait n intervals before running again.

**Function Signature:** `def leastInterval(tasks: List[str], n: int) -> int`

**Example:**

- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`
- Execution: `A -> B -> idle -> A -> B -> idle -> A -> B`

**Skills tested:** Max heap + frequency, greedy scheduling with cooldowns

---

### 12. SingleThreadedCPU

Given tasks with enqueue time and processing time, return the order tasks are processed by a single-threaded CPU (shortest processing time first, ties by index).

**Function Signature:** `def getOrder(tasks: List[List[int]]) -> List[int]`

**Example:**

- Input: `tasks = [[1,2],[2,4],[3,2],[4,1]]`
- Output: `[0,2,3,1]`

**Skills tested:** Min heap with custom ordering, simulation

---

## Advanced Problems

### 13. SlidingWindowMedian

Find the median in each sliding window of size k.

**Function Signature:** `def medianSlidingWindow(nums: List[int], k: int) -> List[float]`

**Example:**

- Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- Output: `[1,-1,-1,3,5,6]`

**Skills tested:** Two heaps with removal, sliding window maintenance

---

### 14. MinimumCostToConnectSticks

Connect sticks with minimum cost. Cost to connect two sticks is their sum.

**Function Signature:** `def connectSticks(sticks: List[int]) -> int`

**Example:**

- Input: `[2,4,3]`
- Connect 2+3=5 (cost 5), then 5+4=9 (cost 9)
- Total cost: 14

**Skills tested:** Min heap, greedy algorithm (Huffman coding pattern)

---

### 15. ReorganizeString

Rearrange characters in a string so no two adjacent characters are the same. Return "" if impossible.

**Function Signature:** `def reorganizeString(s: str) -> str`

**Example:**

- Input: `"aab"`
- Output: `"aba"`
- Input: `"aaab"`
- Output: `""` (impossible)

**Skills tested:** Max heap with frequency, greedy placement

---

### 16. UglyNumberII

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Find the nth ugly number.

**Function Signature:** `def nthUglyNumber(n: int) -> int`

**Example:**

- Sequence: `1, 2, 3, 4, 5, 6, 8, 9, 10, 12...`
- Input: `n = 10`
- Output: `12`

**Skills tested:** Min heap for generating sequence, avoiding duplicates

---

### 17. IPO

You have k projects and limited capital w. Each project has profit and required capital. Maximize final capital.

**Function Signature:** `def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int`

**Example:**

- Input: `k=2`, `w=0`, `profits=[1,2,3]`, `capital=[0,1,1]`
- Output: `4` (do project 0 first, then project 1 or 2)

**Skills tested:** Two heaps (available projects + max profit), greedy selection

---

### 18. MinimumNumberOfRefuelingStops

Find minimum refueling stops to reach target. Each station has position and fuel amount.

**Function Signature:** `def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int`

**Example:**

- Input: `target=100`, `startFuel=10`, `stations=[[10,60],[20,30],[30,30],[60,40]]`
- Output: `2`

**Skills tested:** Max heap for greedy fuel selection, dynamic programming alternative

---

## Design Problems

### 19. DesignTwitter (Heap-based)

Design Twitter with heap for timeline generation.

**Methods to implement:**

- `postTweet(userId, tweetId)`
- `getNewsFeed(userId)` - Return 10 most recent tweet IDs
- `follow(followerId, followeeId)`
- `unfollow(followerId, followeeId)`

**Skills tested:** Min heap for k-way merge, timestamp ordering

---

### 20. KthLargestInStream

Design a class to find the kth largest element in a stream.

**Methods to implement:**

- `KthLargest(k, nums)` - Initialize with k and initial numbers
- `add(val)` - Add a number and return kth largest

**Example:**

```t
kthLargest = KthLargest(3, [4,5,8,2])
kthLargest.add(3)  # returns 4
kthLargest.add(5)  # returns 5
kthLargest.add(10) # returns 5
```

**Skills tested:** Min heap of size k, streaming data

---

## Tips for Practice

1. **Min vs Max:** Understand when to use min heap vs max heap
2. **Size-K Heaps:** For kth largest, use min heap of size k; for kth smallest, use max heap of size k
3. **Custom Comparators:** Learn to define custom comparison for complex objects
4. **Two-Heap Pattern:** Median finding uses max heap (left half) + min heap (right half)
5. **Heap as Priority Queue:** Many scheduling problems are priority queue problems in disguise
6. **Time Complexity:** Heapify is O(n), but insertion is O(log n)

## Common Heap Patterns

- **Top-K Problems:** Maintain heap of size k
- **K-Way Merge:** Use heap to merge k sorted sequences
- **Running Median:** Two heaps (max + min)
- **Scheduling:** Priority queue for task management
- **Frequency-Based:** Combine HashMap with heap
- **Greedy Selection:** Always pick min/max efficiently
- **Stream Processing:** Maintain heap as data arrives

## Python Heap Notes

```python
import heapq

# Min heap (default)
heap = []
heapq.heappush(heap, 5)
heapq.heappop(heap)

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
largest = -heapq.heappop(max_heap)

# Heapify existing list
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)  # O(n)

# Get k largest/smallest
heapq.nlargest(k, nums)
heapq.nsmallest(k, nums)
```
