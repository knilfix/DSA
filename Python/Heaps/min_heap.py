class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_val

    def get_parent(self, i):
        return (i - 1) // 2

    def get_left_child(self, i):
        return (2 * i) + 1

    def get_right_child(self, i):
        return (2 * i) + 2

    def heapify_down(self, i):
        largest = i
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        size = len(self.heap)

        # Fixed: proper condition checks
        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)  # Fixed: added recursion

    def heapify_up(self, i):
        while i > 0:
            parent = self.get_parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def build_heap(self, arr):
        self.heap = arr[:]
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.heapify_down(i)


if __name__ == "__main__":
    nums = [73, 15, 92, 44, 28, 61, 8, 37, 55, 19, 82, 66, 41, 5, 77]
    print(f"Length of nums: {len(nums)}")
    # Create heap
    heap = MaxHeap()

    # Method 1: Build heap from array (efficient O(n))
    print("Before build_heap:", nums)
    heap.build_heap(nums)
    print("After build_heap:", heap.heap)
    print("Max element:", heap.heap[0])  # Should be 92

    # Method 2: Or insert one by one (O(n log n))
    heap2 = MaxHeap()
    for num in nums:
        heap2.insert(num)
    print("\nAfter individual inserts:", heap2.heap)

    # Extract some maximums
    print("\nExtracting maximums:")
    print("1st max:", heap.extract_max())  # Should be 92
    print("2nd max:", heap.extract_max())  # Should be 82
    print("3rd max:", heap.extract_max())  # Should be 77ls

    print("Heap after extractions:", heap.heap)

    # Insert a new value
    heap.insert(95)
    print("\nAfter inserting 95:", heap.heap)
    print("New max:", heap.heap[0])  # Should be 95
