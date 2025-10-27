from linked_list.linked_list import LinkedList


# Test the new functionality
ll = LinkedList()
for i in range(10, 51, 5):
    ll.prepend(i)


# Access by index using get()
print("Third element:", ll.get(2))  # 30
print("First element:", ll.get(0))  # 10

# Access by index using [] syntax (now works!)
print("Second element:", ll[1])  # 20
print("Last element:", ll[-1])  # 50

# Iterate through all
print("All elements:")
sum = 0
for data in ll:
    sum += data
print(f"Sum : {sum}")
mean = sum / ll.size
print(f"Mean: {mean}")

# Output: 10 20 30 40 50

# Convert to list
print("\nAs list:", list(ll))
