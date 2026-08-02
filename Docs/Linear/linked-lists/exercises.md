# Linked List Practice Exercises

## Basic Traversal & Access

### 1. Count()

Write a function that counts the number of times a given value occurs in a linked list.

**Function Signature:** `int count(Node* head, int value)`

**Example:**

- List: `1 -> 2 -> 3 -> 2 -> 4`
- `count(head, 2)` returns `2`
- `count(head, 5)` returns `0`

**Skills tested:** Basic traversal, counting logic

---

### 2. GetNth()

Write a function that returns the data value at a given index position (0-based indexing). If the index is out of bounds, return -1 or throw an error.

**Function Signature:** `int getNth(Node* head, int index)`

**Example:**

- List: `42 -> 13 -> 666`
- `getNth(head, 0)` returns `42`
- `getNth(head, 2)` returns `666`
- `getNth(head, 5)` returns `-1` (or error)

**Skills tested:** Indexed access, bounds checking

---

### 3. Length()

Write a function that returns the number of nodes in a linked list.

**Function Signature:** `int length(Node* head)`

**Example:**

- List: `1 -> 2 -> 3 -> 4`
- `length(head)` returns `4`
- Empty list returns `0`

**Skills tested:** Complete traversal, counting

---

## Insertion Operations

### 4. InsertNth()

Write a function that inserts a new node at a given index position. If index is 0, insert at the head. If index equals length, insert at the tail.

**Function Signature:** `void insertNth(Node** head, int index, int data)`

**Example:**

- List: `1 -> 2 -> 3`
- `insertNth(&head, 1, 99)` → `1 -> 99 -> 2 -> 3`
- `insertNth(&head, 0, 5)` → `5 -> 1 -> 2 -> 3`

**Skills tested:** Pointer manipulation, edge case handling

---

### 5. SortedInsert()

Given a sorted linked list and a value, insert the value in the correct sorted position.

**Function Signature:** `void sortedInsert(Node** head, int data)`

**Example:**

- Sorted list: `1 -> 3 -> 5 -> 7`
- `sortedInsert(&head, 4)` → `1 -> 3 -> 4 -> 5 -> 7`
- `sortedInsert(&head, 0)` → `0 -> 1 -> 3 -> 5 -> 7`

**Skills tested:** Maintaining sorted order, insertion logic

---

### 6. Append()

Write a function that appends a new node to the end of the list.

**Function Signature:** `void append(Node** head, int data)`

**Example:**

- List: `1 -> 2 -> 3`
- `append(&head, 4)` → `1 -> 2 -> 3 -> 4`

**Skills tested:** Traversal to end, tail insertion

---

## Deletion Operations

### 7. DeleteList()

Write a function that deallocates all memory used by a linked list and sets the head pointer to NULL.

**Function Signature:** `void deleteList(Node** head)`

**Example:**

- After calling `deleteList(&head)`, head should be NULL and all nodes freed

**Skills tested:** Memory management, preventing memory leaks

---

### 8. Pop()

Write a function that deletes the node at the head of the list and returns its data value.

**Function Signature:** `int pop(Node** head)`

**Example:**

- List: `1 -> 2 -> 3`
- `pop(&head)` returns `1`, list becomes `2 -> 3`

**Skills tested:** Head deletion, returning values

---

### 9. RemoveValue()

Write a function that removes the first occurrence of a given value from the list.

**Function Signature:** `void removeValue(Node** head, int value)`

**Example:**

- List: `1 -> 2 -> 3 -> 2 -> 4`
- `removeValue(&head, 2)` → `1 -> 3 -> 2 -> 4`

**Skills tested:** Search and delete, pointer reassignment

---

### 10. DeleteNth()

Write a function that deletes the node at a given index position.

**Function Signature:** `void deleteNth(Node** head, int index)`

**Example:**

- List: `1 -> 2 -> 3 -> 4`
- `deleteNth(&head, 2)` → `1 -> 2 -> 4`

**Skills tested:** Indexed deletion, edge cases

---

## Advanced Operations

### 11. Reverse()

Write a function that reverses a linked list in-place.

**Function Signature:** `void reverse(Node** head)`

**Example:**

- List: `1 -> 2 -> 3 -> 4`
- `reverse(&head)` → `4 -> 3 -> 2 -> 1`

**Skills tested:** Pointer manipulation, iterative reversal

---

### 12. RecursiveReverse()

Write a recursive function that reverses a linked list.

**Function Signature:** `Node* recursiveReverse(Node* head)`

**Example:**

- Same as above, but using recursion

**Skills tested:** Recursive thinking, pointer manipulation

---

### 13. MergeSorted()

Write a function that takes two sorted linked lists and merges them into one sorted list.

**Function Signature:** `Node* mergeSorted(Node* a, Node* b)`

**Example:**

- List A: `1 -> 3 -> 5`
- List B: `2 -> 4 -> 6`
- Result: `1 -> 2 -> 3 -> 4 -> 5 -> 6`

**Skills tested:** Two-pointer technique, maintaining sorted order

---

### 14. RemoveDuplicates()

Given a sorted linked list, remove all duplicate values.

**Function Signature:** `void removeDuplicates(Node* head)`

**Example:**

- List: `1 -> 1 -> 2 -> 3 -> 3 -> 3 -> 4`
- Result: `1 -> 2 -> 3 -> 4`

**Skills tested:** In-place modification, deletion logic

---

### 15. HasCycle()

Write a function that detects if a linked list has a cycle (Floyd's algorithm).

**Function Signature:** `bool hasCycle(Node* head)`

**Example:**

- List with cycle: returns `true`
- List without cycle: returns `false`

**Skills tested:** Two-pointer technique, cycle detection

---

## Challenging Problems

### 16. FindMiddle()

Write a function that returns the middle node of a linked list. If there are two middle nodes, return the second one.

**Function Signature:** `Node* findMiddle(Node* head)`

**Example:**

- List: `1 -> 2 -> 3 -> 4 -> 5`
- Returns node with value `3`

**Skills tested:** Fast/slow pointer technique

---

### 17. IsPalindrome()

Write a function that checks if a linked list is a palindrome.

**Function Signature:** `bool isPalindrome(Node* head)`

**Example:**

- List: `1 -> 2 -> 3 -> 2 -> 1` returns `true`
- List: `1 -> 2 -> 3` returns `false`

**Skills tested:** Multiple traversals, comparison logic

---

### 18. Partition()

Given a value x, partition the list such that all nodes less than x come before all nodes greater than or equal to x. Preserve original relative order.

**Function Signature:** `Node* partition(Node* head, int x)`

**Example:**

- List: `3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1`, x = 5
- Result: `3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10`

**Skills tested:** List manipulation, maintaining order

---

### 19. RotateRight()

Rotate the linked list to the right by k positions.

**Function Signature:** `Node* rotateRight(Node* head, int k)`

**Example:**

- List: `1 -> 2 -> 3 -> 4 -> 5`, k = 2
- Result: `4 -> 5 -> 1 -> 2 -> 3`

**Skills tested:** Circular list concepts, modular arithmetic

---

### 20. AlternatingSplit()

Split a linked list into two lists where nodes alternate between the two lists.

**Function Signature:** `void alternatingSplit(Node* source, Node** aRef, Node** bRef)`

**Example:**

- Source: `1 -> 2 -> 3 -> 4 -> 5 -> 6`
- List A: `1 -> 3 -> 5`
- List B: `2 -> 4 -> 6`

**Skills tested:** Multiple list manipulation, alternating logic

---

## Tips for Practice

1. **Start Simple:** Master basic traversal before moving to complex operations
2. **Draw It Out:** Sketch linked list diagrams before coding
3. **Edge Cases:** Always test with empty lists, single nodes, and two nodes
4. **Memory Management:** For languages with manual memory management, always free deleted nodes
5. **Pointer Mastery:** Understand when to use `Node*` vs `Node**`
6. **Test Thoroughly:** Create test cases for each function before implementing

## Common Pitfalls to Avoid

- Forgetting to update head pointer when modifying the first node
- Not handling empty list cases
- Memory leaks when deleting nodes
- Off-by-one errors in indexed operations
- Not maintaining list integrity (broken links)
