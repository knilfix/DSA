class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")

        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return

    def dequeue(self):
        if self.is_empty():
            return None

        data = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0


def main():
    # Create a circular buffer of size 3
    cb = CircularBuffer(3)

    print("Initial state:")
    print(f"Empty: {cb.is_empty()}, Full: {cb.is_full()}")
    print()

    # Test Enqueue
    print("Enqueuing A, B, C...")
    cb.enqueue("A")
    cb.enqueue("B")
    cb.enqueue("C")
    print(f"Empty: {cb.is_empty()}, Full: {cb.is_full()}")
    print()

    # Test trying to enqueue when full
    print("Trying to enqueue D (should fail)...")
    try:
        cb.enqueue("D")
    except Exception as e:
        print(f"Error: {e}")
    print()

    # Test Dequeue
    print("Dequeuing two items...")
    print("Dequeued:", cb.dequeue())  # Should be A
    print("Dequeued:", cb.dequeue())  # Should be B
    print(f"Empty: {cb.is_empty()}, Full: {cb.is_full()}")
    print()

    # Test Enqueue again after dequeue (testing wrap-around)
    print("Enqueuing D (should wrap around)...")
    cb.enqueue("D")
    print(f"Empty: {cb.is_empty()}, Full: {cb.is_full()}")
    print()

    # Test Dequeue until empty
    print("Dequeuing until empty...")
    print("Dequeued:", cb.dequeue())  # Should be C
    print("Dequeued:", cb.dequeue())  # Should be D
    print("Dequeued:", cb.dequeue())  # Should be None (empty)
    print(f"Empty: {cb.is_empty()}, Full: {cb.is_full()}")


if __name__ == "__main__":
    main()
