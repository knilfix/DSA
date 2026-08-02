# HashMaps

## 🧩 **Definition**

A **Hashmap** (or **Hash Table**) is a data structure that stores **key–value pairs** and provides *average* **O(1)** access, insertion, and deletion by using a **hash function** to compute an index into an internal array of buckets.

---

## 💡 **Core Idea**

The core idea behind a hashmap is **direct addressing** without linear search.
Instead of looking through a list of keys, the key is *hashed* into a numerical index, which directly points to where the value should live.

---

## ⚙️ **Key Operations**

| Operation            | Description                             | Time Complexity          |
| -------------------- | --------------------------------------- | ------------------------ |
| `insert(key, value)` | Hashes key, stores pair in bucket       | O(1) average, O(n) worst |
| `get(key)`           | Retrieves value by key                  | O(1) average, O(n) worst |
| `delete(key)`        | Removes pair by key                     | O(1) average, O(n) worst |
| `rehash()`           | Resizes internal array and re-maps keys | O(n)                     |

---

## 🧱 **Internal Concept**

A hashmap internally uses an **array of buckets**.
Each **bucket** holds a **linked list (or dynamic structure)** of key–value pairs that hash to the same index — this is how **collisions** are handled.

```t
          +------------------------------------------------+
          |     Array of Buckets (size = N)                |
          +------------------------------------------------+
            0       1       2       3       4       5
            |       |       |       |       |       |
            ↓       ↓       ↓       ↓       ↓       ↓
           None   [A:1] → [F:6]   [C:3]   None   [Z:26] → [L:12]
```

* The **array** is like an address book.
* Each **bucket** is either `None` (empty) or points to a linked list of key–value pairs.
* Each **node** in the list holds:

  * The **key**
  * The **value**
  * A **pointer** to the next node in that bucket

When collisions pile up (too many keys in one bucket), performance can degrade — hence the need for **rehashing** when the load factor exceeds a threshold (commonly `0.75`).

---

## 🧭 **Use Cases**

* Dictionaries and symbol tables
* Caches (e.g., LRU cache)
* Counting frequencies (word frequency, histograms)
* Indexing objects by unique IDs or strings
* Implementing sets (hash sets)

---

## 🧮 **Complexity Overview**

| Operation | Average | Worst |
| --------- | ------- | ----- |
| Insert    | O(1)    | O(n)  |
| Search    | O(1)    | O(n)  |
| Delete    | O(1)    | O(n)  |
| Space     | O(n)    | O(n)  |

---

## 🧰 **Implementation References**

* **Python:** [../Python/Hashmaps/hash_map.py](../Python/Hashmaps/hash_map.py), [../Python/Hashmaps/use_hash_map.py](../Python/Hashmaps/use_hash_map.py)
* **C:** [../C/NonLinearDataStructures/Hashmaps/hashmap.c](../C/NonLinearDataStructures/Hashmaps/hashmap.c)

---

## 🧠 **Notes & Insights**

* The **array** stores **buckets** (pointers to lists, not the data directly).
* The **linked list nodes** inside buckets hold the *actual data*.
* Good hash functions minimize collisions by spreading keys uniformly.
* Modern implementations (like Python’s dict) optimize further using **open addressing** and **dynamic resizing**.
* Performance relies heavily on maintaining a low **load factor**.

> [!tip]
> Hashmaps are ideal when lookup time matters more than order.

---
