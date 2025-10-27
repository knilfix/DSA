class HashTable:
    """A hash table implementation using separate chaining for collision resolution.

    Features:
    - Dynamic resizing when load factor exceeds 0.8
    - Prime number capacity for better distribution
    - Support for any hashable key type
    - Average O(1) time complexity for operations
    """

    def __init__(self, capacity) -> None:
        """Initialize hash table with given initial capacity.

        Args:
            capacity: Initial number of buckets (will be adjusted to next prime if needed)
        """
        self.bucket_array = [None] * capacity
        self.capacity = capacity
        self.size = 0  # Number of key-value pairs stored

    def put(self, key, value):
        """Insert or update a key-value pair.

        Args:
            key: Hashable key (any type supported by Python's hash())
            value: Associated value to store

        Time Complexity: O(1) average, O(n) worst-case during rehashing
        """
        index = self._hash(key)

        # Initialize bucket if empty
        if self.bucket_array[index] is None:
            self.bucket_array[index] = HashTableBucket()

        bucket = self.bucket_array[index]
        existing_entry = bucket.find(key)

        if existing_entry:
            # Key exists - update value
            existing_entry.value = value
        else:
            # Key doesn't exist - check if we need to rehash before inserting
            if (self.size + 1) / self.capacity >= 0.8:
                self.rehash()  # This replaces bucket_array entirely!

                # After rehash, must re-locate the bucket in the new array
                index = self._hash(key)
                if self.bucket_array[index] is None:
                    self.bucket_array[index] = HashTableBucket()
                bucket = self.bucket_array[index]  # Critical: Get bucket from NEW array

            bucket.insert_at_beginning(key, value)
            self.size += 1

    def get(self, key):
        """Retrieve value associated with key, or None if not found.

        Args:
            key: Key to search for

        Returns:
            Value associated with key, or None if key doesn't exist

        Time Complexity: O(1) average, O(n) worst-case (all keys in same bucket)
        """
        index = self._hash(key)
        bucket = self.bucket_array[index]

        if bucket is None:
            return None

        entry = bucket.find(key)
        return entry.value if entry is not None else None

    def remove(self, key):
        """Remove key-value pair from hash table.

        Args:
            key: Key to remove

        Returns:
            True if key was found and removed, False otherwise

        Time Complexity: O(1) average, O(n) worst-case
        """
        index = self._hash(key)
        bucket = self.bucket_array[index]

        if bucket is None:
            return False

        if bucket.delete(key):
            self.size -= 1
            return True
        return False

    # --- Helper Methods ---

    def _hash(self, key) -> int:
        """Compute bucket index for a given key.

        Uses Python's built-in hash() function with modulo operation
        to distribute keys evenly across buckets.
        """
        hash_code = hash(key)
        return hash_code % self.capacity  # Ensure index is within bounds

    def rehash(self):
        """Resize hash table to next prime number (2x current capacity).

        Reinserts all existing key-value pairs into new larger table.
        This is triggered automatically when load factor exceeds 0.8.
        """
        old_bucket_array = self.bucket_array
        old_capacity = self.capacity

        # Find appropriate new size (prime number for better distribution)
        new_capacity = self.next_prime(self.capacity * 2)

        # Create new empty bucket array
        self.bucket_array = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0  # Will be rebuilt during reinsertion

        # Reinsert all existing entries into new table
        for bucket in old_bucket_array:
            if bucket is not None:
                current = bucket.head
                while current is not None:
                    # Recalculate index using new capacity
                    new_index = self._hash(current.key)

                    if self.bucket_array[new_index] is None:
                        self.bucket_array[new_index] = HashTableBucket()

                    # Insert into appropriate bucket in new array
                    self.bucket_array[new_index].insert_at_beginning(
                        current.key, current.value
                    )
                    self.size += 1
                    current = current.next

    def print_table(self):
        """Display current state of hash table for debugging."""
        print(f"\nHash Table (Capacity: {self.capacity}, Size: {self.size})")
        print("=" * 50)

        for i, bucket in enumerate(self.bucket_array):
            print(f"Bucket {i}: ", end="")

            if bucket is None:
                print("Empty")
            else:
                # Display chain of entries in this bucket
                current = bucket.head
                entries = []
                while current:
                    entries.append(f"{current.key}:{current.value}")
                    current = current.next
                print(" -> ".join(entries) if entries else "Empty")

    def next_prime(self, n):
        """Find smallest prime number greater than n.

        Prime number capacities help reduce clustering and improve
        hash function distribution.
        """

        def is_prime(num):
            """Check if number is prime using trial division."""
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            # Check odd divisors up to sqrt(num)
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        # Start from n+1 and search for next prime
        candidate = n + 1
        while True:
            if is_prime(candidate):
                return candidate
            candidate += 1


class HashTableEntry:
    """Represents a single key-value pair in the hash table.

    Also serves as a node in the linked list for chaining.
    """

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None  # Pointer to next entry in chain (for collisions)


class HashTableBucket:
    """Represents a bucket in the hash table using linked list chaining.

    Handles collision resolution by storing multiple entries in a linked list.
    """

    def __init__(self) -> None:
        self.head = None  # Head of linked list

    def insert_at_beginning(self, key, value):
        """Insert new entry at beginning of chain (O(1) operation)."""
        if self.head is None:
            self.head = HashTableEntry(key=key, value=value)
            return

        new_entry = HashTableEntry(key=key, value=value)
        new_entry.next = self.head
        self.head = new_entry

    def delete(self, key):
        """Remove entry with given key from chain.

        Returns:
            True if key was found and removed, False otherwise
        """
        if self.head is None:
            return False

        # Special case: remove head
        if self.head.key == key:
            self.head = self.head.next
            return True

        # Search for key in rest of list
        current = self.head
        while current.next:
            if current.next.key == key:
                current.next = current.next.next  # Bypass node to delete
                return True
            current = current.next

        return False  # Key not found

    def find(self, key) -> HashTableEntry:
        """Search for entry with given key in chain.

        Returns:
            HashTableEntry if found, None otherwise
        """
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None


if __name__ == "__main__":
    # Demonstration of hash table functionality
    dictionary = HashTable(10)

    # Various data types as keys and values
    dictionary.put(key="age", value=25)
    dictionary.put(key="name", value="Alice")
    dictionary.put(key=42, value=["apple", "banana", "cherry"])
    dictionary.put(key="address", value={"street": "123 Main St", "city": "Boston"})
    dictionary.put(key=3.14, value=True)

    dictionary.print_table()

    # Test retrievals
    print(f"\nRetrievals:")
    print(f"age: {dictionary.get('age')}")
    print(f"42: {dictionary.get(42)}")
    print(f"address: {dictionary.get('address')}")
