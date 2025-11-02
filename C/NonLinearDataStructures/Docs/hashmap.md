## Hash Table

**Purpose**: Key-value storage with average O(1) access time  
**Core Idea**: Array of buckets + hash function + collision resolution  

**Structure**:

```
HashTable:
  - bucket_array: array of buckets
  - capacity: integer (number of buckets)
  - size: integer (number of key-value pairs)

HashTableBucket:
  - head: pointer to HashTableEntry (linked list)

HashTableEntry:
  - key: any hashable type
  - value: any data  
  - next: pointer to next entry
```

**Key Operations**:

- `put()`: O(1) average (O(n) with rehashing)
- `get()`: O(1) average (O(n) worst-case)
- `remove()`: O(1) average (O(n) worst-case)
- `rehash()`: O(n) - resizes when load factor > 0.75

**Collision Resolution**: Separate chaining (linked lists)  
**Load Factor**: 0.75 trigger for resizing  
**Resize Strategy**: Double capacity + find next prime number

---

## Quick Notes

- **Hash Function**: `hash(key) % capacity`
- **Prime Capacity**: Better distribution, reduces clustering
- **Separate Chaining**: Linked list in each bucket for collisions
- **Load Factor**: size/capacity - tradeoff between space and performance
- **Good for**: Dictionaries, caches, frequency counting
- **Bad for**: Ordered data, range queries

---

## Key Implementation Details

- **Rehashing**: Create new array, reinsert all elements
- **Prime Numbers**: Reduce hash collisions via better distribution
- **Memory**: Array + linked lists overhead
- **Edge Cases**: Empty buckets, single collisions, full rehash

---

## 🎯 **Your Python Implementation is EXCELLENT!**

**What's Impressive:**

- ✅ Proper separate chaining
- ✅ Dynamic resizing with prime numbers  
- ✅ Clean object-oriented design
- ✅ Good documentation and edge case handling
- ✅ Multiple data type support

**For C Version - Key Differences:**

```c
// Instead of classes
typedef struct HashEntry {
    void* key;
    void* value;
    struct HashEntry* next;
} HashEntry;

typedef struct HashTable {
    HashEntry** buckets;
    int capacity;
    int size;
} HashTable;
```

**Don't Be Scared!** You already understand the concepts perfectly. The C version is just:

- Manual memory management (malloc/free)
- Function pointers for hashing/comparison
- Array of pointers instead of Python lists

You've got this! Your conceptual foundation is rock solid! 💪🚀
