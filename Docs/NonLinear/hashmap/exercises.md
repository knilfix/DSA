# Dictionary/HashMap Practice Exercises

> **Note:** Dictionary (Python) and HashMap (Java/C++) refer to the same ADT - a key-value data structure with O(1) average lookup time.

## Basic Operations

### 1. TwoSum

Given an array of integers and a target, return indices of two numbers that add up to the target.

**Function Signature:** `def twoSum(nums: List[int], target: int) -> List[int]`

**Example:**

- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]` (because nums[0] + nums[1] = 9)

**Skills tested:** HashMap for O(n) lookup, complement pattern

---

### 2. ContainsDuplicate

Given an array, return true if any value appears at least twice.

**Function Signature:** `def containsDuplicate(nums: List[int]) -> bool`

**Example:**

- Input: `[1, 2, 3, 1]`
- Output: `True`

**Skills tested:** Set/HashMap for tracking seen elements

---

### 3. FirstUniqueCharacter

Find the first non-repeating character in a string and return its index. Return -1 if none exists.

**Function Signature:** `def firstUniqChar(s: str) -> int`

**Example:**

- Input: `"leetcode"`
- Output: `0` (character 'l' appears only once)
- Input: `"loveleetcode"`
- Output: `2` (character 'v')

**Skills tested:** Frequency counting with HashMap

---

## Frequency & Counting

### 4. GroupAnagrams

Given an array of strings, group anagrams together.

**Function Signature:** `def groupAnagrams(strs: List[str]) -> List[List[str]]`

**Example:**

- Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`

**Skills tested:** HashMap with computed keys, sorting as key

---

### 5. TopKFrequentElements

Given an array and integer k, return the k most frequent elements.

**Function Signature:** `def topKFrequent(nums: List[int], k: int) -> List[int]`

**Example:**

- Input: `nums = [1,1,1,2,2,3]`, `k = 2`
- Output: `[1, 2]`

**Skills tested:** Frequency HashMap, sorting/heap for top-K

---

### 6. SubarraySumEqualsK

Find the total number of continuous subarrays whose sum equals k.

**Function Signature:** `def subarraySum(nums: List[int], k: int) -> int`

**Example:**

- Input: `nums = [1,1,1]`, `k = 2`
- Output: `2` (subarrays [1,1] appear twice)

**Skills tested:** Prefix sum + HashMap, cumulative sum technique

---

### 7. LongestConsecutiveSequence

Find the length of the longest consecutive elements sequence in an unsorted array. Must run in O(n) time.

**Function Signature:** `def longestConsecutive(nums: List[int]) -> int`

**Example:**

- Input: `[100, 4, 200, 1, 3, 2]`
- Output: `4` (sequence [1, 2, 3, 4])

**Skills tested:** Set operations, sequence building

---

## Design & Implementation

### 8. DesignHashMap

Design a HashMap without using built-in hash table libraries.

**Methods to implement:**

- `put(key, value)` - Insert or update key-value pair
- `get(key)` - Return value for key, or -1 if not exists
- `remove(key)` - Remove key-value pair if exists

**Example:**

```t
hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)      # returns 1
hashMap.get(3)      # returns -1
hashMap.put(2, 1)   # update
hashMap.get(2)      # returns 1
hashMap.remove(2)
hashMap.get(2)      # returns -1
```

**Skills tested:** Hash function, collision handling, array + linked list

---

### 9. LRUCache

Design a Least Recently Used (LRU) cache with O(1) get and put operations.

**Methods to implement:**

- `get(key)` - Return value if exists, else -1 (mark as recently used)
- `put(key, value)` - Insert/update and mark as recently used (evict LRU if full)

**Example:**

```t
cache = LRUCache(2)  # capacity = 2
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)         # returns 1
cache.put(3, 3)      # evicts key 2
cache.get(2)         # returns -1 (evicted)
cache.put(4, 4)      # evicts key 1
cache.get(1)         # returns -1
cache.get(3)         # returns 3
cache.get(4)         # returns 4
```

**Skills tested:** HashMap + Doubly Linked List, O(1) operations

---

### 10. DesignTwitter

Design a simplified Twitter with posting tweets and news feed features.

**Methods to implement:**

- `postTweet(userId, tweetId)` - Create a new tweet
- `getNewsFeed(userId)` - Get 10 most recent tweets from user and their followees
- `follow(followerId, followeeId)` - Follower follows a followee
- `unfollow(followerId, followeeId)` - Follower unfollows a followee

**Skills tested:** Multiple HashMaps, timestamp ordering, graph relationships

---

## String & Pattern Matching

### 11. IsomorphicStrings

Two strings are isomorphic if characters in s can be replaced to get t (maintaining order).

**Function Signature:** `def isIsomorphic(s: str, t: str) -> bool`

**Example:**

- Input: `s = "egg"`, `t = "add"`
- Output: `True` (e->a, g->d)
- Input: `s = "foo"`, `t = "bar"`
- Output: `False` (o cannot map to both a and r)

**Skills tested:** Bidirectional mapping with two HashMaps

---

### 12. WordPattern

Given a pattern and a string s, find if s follows the same pattern.

**Function Signature:** `def wordPattern(pattern: str, s: str) -> bool`

**Example:**

- Input: `pattern = "abba"`, `s = "dog cat cat dog"`
- Output: `True`
- Input: `pattern = "abba"`, `s = "dog cat cat fish"`
- Output: `False`

**Skills tested:** Bijection mapping, pattern matching

---

### 13. MinimumWindowSubstring

Find the minimum window substring of s that contains all characters of t.

**Function Signature:** `def minWindow(s: str, t: str) -> str`

**Example:**

- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Output: `"BANC"`

**Skills tested:** Sliding window + HashMap, character frequency tracking

---

## Advanced Problems

### 14. LongestSubstringWithoutRepeating

Find the length of the longest substring without repeating characters.

**Function Signature:** `def lengthOfLongestSubstring(s: str) -> int`

**Example:**

- Input: `"abcabcbb"`
- Output: `3` (substring "abc")
- Input: `"pwwkew"`
- Output: `3` (substring "wke")

**Skills tested:** Sliding window + HashMap, dynamic window sizing

---

### 15. FourSum

Find all unique quadruplets in an array that sum to a target.

**Function Signature:** `def fourSum(nums: List[int], target: int) -> List[List[int]]`

**Example:**

- Input: `nums = [1,0,-1,0,-2,2]`, `target = 0`
- Output: `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

**Skills tested:** HashMap optimization, k-sum pattern

---

### 16. RandomizedSet

Design a data structure supporting insert, remove, and getRandom in O(1) average time.

**Methods to implement:**

- `insert(val)` - Insert value, return true if not present
- `remove(val)` - Remove value, return true if present
- `getRandom()` - Return random element with equal probability

**Skills tested:** HashMap + Dynamic Array, constant time operations

---

### 17. ValidSudoku

Determine if a 9x9 Sudoku board is valid (no duplicate numbers in rows, columns, or 3x3 boxes).

**Function Signature:** `def isValidSudoku(board: List[List[str]]) -> bool`

**Skills tested:** Multiple HashMaps/Sets, 2D grid processing

---

### 18. EncodeAndDecodeStrings

Design an algorithm to encode a list of strings to a single string, and decode it back.

**Methods to implement:**

- `encode(strs: List[str]) -> str`
- `decode(s: str) -> List[str]`

**Example:**

- Input: `["Hello", "World"]`
- Encode: `"5#Hello5#World"` (or your own format)
- Decode back to: `["Hello", "World"]`

**Skills tested:** String serialization, delimiter handling

---

## Graph & Relationship Problems

### 19. CloneGraph

Clone a connected undirected graph where each node contains a value and a list of neighbors.

**Function Signature:** `def cloneGraph(node: Node) -> Node`

**Skills tested:** HashMap for node mapping, graph traversal (DFS/BFS)

---

### 20. CourseSchedule

Given course prerequisites, determine if it's possible to finish all courses (detect cycle in directed graph).

**Function Signature:** `def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool`

**Example:**

- Input: `numCourses = 2`, `prerequisites = [[1,0]]`
- Output: `True` (take course 0, then course 1)
- Input: `numCourses = 2`, `prerequisites = [[1,0],[0,1]]`
- Output: `False` (circular dependency)

**Skills tested:** Graph representation with HashMap, cycle detection

---

## Tips for Practice

1. **Key Choice Matters:** Think carefully about what to use as keys
2. **Frequency Pattern:** HashMap is perfect for counting occurrences
3. **Two-Pass vs One-Pass:** Sometimes building the map first simplifies logic
4. **Complementary Lookups:** Store what you're looking for (e.g., target - current)
5. **Multiple Maps:** Don't hesitate to use 2-3 HashMaps if it clarifies logic

## Common HashMap Patterns

- **Frequency Counting:** Count occurrences of elements
- **Complement Pattern:** Store and lookup complements (TwoSum)
- **Grouping:** Use computed keys to group related items
- **Caching:** Store computed results for reuse (memoization)
- **Graph Representation:** Adjacency list using HashMap
- **Index Mapping:** Map values to their positions
- **Sliding Window:** Track character/element frequencies in windows
