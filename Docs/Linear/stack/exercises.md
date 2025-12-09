# Stack Practice Exercises

## Basic Operations

### 1. MinStack

Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

**Methods to implement:**

- `push(val)` - Push element val onto stack
- `pop()` - Remove the element on top of the stack
- `top()` - Get the top element
- `getMin()` - Retrieve the minimum element in O(1)

**Example:**

```t
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
stack.getMin()  # returns -3
stack.pop()
stack.top()     # returns 0
stack.getMin()  # returns -2
```

**Skills tested:** Auxiliary data structures, constant time operations

---

### 2. ValidParentheses

Given a string containing just the characters `'(', ')', '{', '}', '[', ']'`, determine if the input string is valid (all brackets properly closed and in correct order).

**Function Signature:** `def isValid(s: str) -> bool`

**Examples:**

- `"()"` → `True`
- `"()[]{}"` → `True`
- `"(]"` → `False`
- `"([)]"` → `False`
- `"{[]}"` → `True`

**Skills tested:** Stack matching, string processing

---

### 3. EvaluateReversePolishNotation

Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix notation).

**Function Signature:** `def evalRPN(tokens: List[str]) -> int`

**Example:**

- `["2", "1", "+", "3", "*"]` → `9` (equivalent to `(2 + 1) * 3`)
- `["4", "13", "5", "/", "+"]` → `6` (equivalent to `4 + (13 / 5)`)

**Valid operators:** `+`, `-`, `*`, `/`

**Skills tested:** Expression evaluation, operator precedence

---

## String & Text Problems

### 4. SimplifyPath

Given an absolute path for a Unix-style file system, simplify it by resolving `.` and `..`.

**Function Signature:** `def simplifyPath(path: str) -> str`

**Examples:**

- `"/home/"` → `"/home"`
- `"/a/./b/../../c/"` → `"/c"`
- `"/a/../../b/../c//.//"` → `"/c"`

**Rules:**

- `.` means current directory
- `..` means parent directory
- Multiple slashes = single slash
- Result must start with `/`

**Skills tested:** Path parsing, stack-based navigation

---

### 5. DecodeString

Given an encoded string like `"3[a]2[bc]"`, return the decoded string `"aaabcbc"`.

**Function Signature:** `def decodeString(s: str) -> str`

**Examples:**

- `"3[a]2[bc]"` → `"aaabcbc"`
- `"3[a2[c]]"` → `"accaccacc"`
- `"2[abc]3[cd]ef"` → `"abcabccdcdcdef"`

**Skills tested:** Nested structures, string building

---

### 6. RemoveAdjacentDuplicates

Given a string, remove all adjacent duplicate characters recursively.

**Function Signature:** `def removeDuplicates(s: str) -> str`

**Examples:**

- `"abbaca"` → `"ca"` (remove "bb", then "aa")
- `"azxxzy"` → `"ay"` (remove "xx", then "zz")

**Skills tested:** Stack-based removal, iterative processing

---

## Monotonic Stack Problems

### 7. DailyTemperatures

Given a list of daily temperatures, return a list where each element is the number of days you have to wait until a warmer temperature. If there's no future warmer day, use 0.

**Function Signature:** `def dailyTemperatures(temps: List[int]) -> List[int]`

**Example:**

- Input: `[73, 74, 75, 71, 69, 72, 76, 73]`
- Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

**Skills tested:** Monotonic stack, next greater element pattern

---

### 8. NextGreaterElement

Given an array, find the next greater element for every element. If no greater element exists, use -1.

**Function Signature:** `def nextGreater(arr: List[int]) -> List[int]`

**Example:**

- Input: `[4, 5, 2, 25]`
- Output: `[5, 25, 25, -1]`

**Skills tested:** Monotonic stack, next greater pattern

---

### 9. LargestRectangleInHistogram

Given heights of bars in a histogram, find the area of the largest rectangle that can be formed.

**Function Signature:** `def largestRectangle(heights: List[int]) -> int`

**Example:**

- Input: `[2, 1, 5, 6, 2, 3]`
- Output: `10` (rectangle with height 5 and width 2)

**Skills tested:** Advanced monotonic stack, area calculation

---

## Design & Implementation

### 10. StackUsingQueues

Implement a stack using only queue operations (FIFO structure).

**Methods to implement:**

- `push(x)` - Push element x onto stack
- `pop()` - Remove and return top element
- `top()` - Get the top element
- `empty()` - Return whether stack is empty

**Challenge:** Make either push or pop O(1) time

**Skills tested:** Data structure conversion, trade-off analysis

---

### 11. SortStack

Sort a stack such that smallest items are on top. You can use an additional temporary stack, but no other data structure.

**Function Signature:** `def sortStack(stack: Stack) -> Stack`

**Example:**

- Input: `[34, 3, 31, 98, 92, 23]` (bottom to top)
- Output: `[98, 92, 34, 31, 23, 3]` (bottom to top, 3 on top)

**Skills tested:** Stack sorting, limited data structure usage

---

## Advanced Problems

### 12. BasicCalculator

Implement a basic calculator to evaluate a simple expression string containing `+`, `-`, `(`, `)`, and non-negative integers.

**Function Signature:** `def calculate(s: str) -> int`

**Examples:**

- `"1 + 1"` → `2`
- `"2-1 + 2"` → `3`
- `"(1+(4+5+2)-3)+(6+8)"` → `23`

**Skills tested:** Expression parsing, handling parentheses

---

### 13. TrappingRainWater (Stack approach)

Given elevation map heights, compute how much water can be trapped after raining.

**Function Signature:** `def trap(height: List[int]) -> int`

**Example:**

- Input: `[0,1,0,2,1,0,1,3,2,1,2,1]`
- Output: `6`

**Skills tested:** Complex monotonic stack application

---

### 14. MaximalRectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's.

**Function Signature:** `def maximalRectangle(matrix: List[List[str]]) -> int`

**Example:**

```t
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

**Skills tested:** Combining histogram problem with 2D thinking

---

## Tips for Practice

1. **Draw It Out:** Visualize stack operations with simple diagrams
2. **Think LIFO:** Remember Last In, First Out - what goes on last comes off first
3. **Edge Cases:** Empty stack, single element, all same elements
4. **Monotonic Stacks:** Master this pattern - it appears frequently in interviews
5. **Space-Time Trade-offs:** Sometimes using an extra stack simplifies the solution

## Common Stack Patterns

- **Matching/Validation:** Parentheses, tags, brackets
- **Backtracking:** Undo operations, path navigation
- **Expression Evaluation:** Postfix, infix, prefix
- **Monotonic Stack:** Next greater/smaller element problems
- **State Management:** Function calls, recursion simulation
