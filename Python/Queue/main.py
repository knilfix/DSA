from array_queue import ArrayQueue
from circular_queue import CircularBuffer
from linked_list_queue import LinkedListQueue

# Test your LinkedListQueue
queue = CircularBuffer(10)
# queue = CircularBuffer()
# queue = ArrayQueue()
print("Initial queue is empty:", queue.is_empty())  # Should be True

queue.enqueue("Customer A")
queue.enqueue("Customer B")
queue.enqueue("Customer C")

print("Peek at the front:", queue.peek())  # Who should be first?
print("Dequeue:", queue.dequeue())  # Who should be removed?

queue.enqueue("Customer D")
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())  # What happens here?
print("Final check is empty:", queue.is_empty())
queue.print_queue()
