from linked_list.linked_list import LinkedList
import random


def comprehensive_test():
    print("=== Comprehensive Linked List Test ===\n")

    ll = LinkedList()

    # Test 1: Empty list operations
    print("1. Testing empty list:")
    print(f"   Is empty: {ll.is_empty()}")
    print(f"   Length: {ll.length()}")
    ll.print_list()
    print(f"   Search 5: {ll.search(5)}")
    print(f"   Delete 5: {ll.delete(5)}")
    print()

    # Test 2: Single node operations
    print("2. Testing single node:")
    ll.append(42)
    print(f"   Length: {ll.length()}")
    ll.print_list()
    print(f"   Search 42: {ll.search(42)}")
    print(f"   Search 99: {ll.search(99)}")
    print()

    # Test 3: Multiple appends
    print("3. Adding multiple nodes (appending):")
    for i in range(10):
        ll.append(i * 10)
    ll.print_list()
    print(f"   Length: {ll.length()}")
    print()

    # Test 4: Prepend operations
    print("4. Testing prepend:")
    ll.prepend(999)
    ll.prepend(888)
    ll.print_list()
    print(f"   Length: {ll.length()}")
    print()

    # Test 5: Insert after
    print("5. Testing insert_after:")
    ll.insert_after(0, 111)  # Insert after existing value
    ll.insert_after(999, 222)  # Insert after head
    ll.insert_after(99999, 333)  # Try non-existent value
    ll.print_list()
    print()

    # Test 6: Search operations
    print("6. Testing search:")
    test_values = [888, 0, 90, 99999]
    for val in test_values:
        print(f"   Search {val}: {ll.search(val)}")
    print()

    # Test 7: Delete operations
    print("7. Testing delete:")
    print(f"   Delete head (888): {ll.delete(888)}")
    print(f"   Delete middle (0): {ll.delete(0)}")
    print(f"   Delete tail (90): {ll.delete(90)}")
    print(f"   Delete non-existent (99999): {ll.delete(99999)}")
    ll.print_list()
    print(f"   Length: {ll.length()}")
    print()

    # Test 8: Reverse
    print("8. Testing reverse:")
    print("   Before reverse:", end=" ")
    ll.print_list()
    ll.reverse()
    print("   After reverse: ", end=" ")
    ll.print_list()
    print()

    # Test 9: Large dataset
    print("9. Testing with large dataset (1000 nodes):")
    big_list = LinkedList()
    for i in range(1000):
        big_list.append(i)

    print(f"   Length: {big_list.length()}")
    print(f"   Head: {big_list.head.data if big_list.head else 'None'}")
    print(f"   Search 500: {big_list.search(500)}")
    print(f"   Search 1500: {big_list.search(1500)}")

    # Test reverse on large list
    big_list.reverse()
    print(f"   Head after reverse: {big_list.head.data if big_list.head else 'None'}")
    print()


def stress_test():
    print("=== Randomized Stress Test ===")

    ll = LinkedList()
    added_values = []

    # Add 500 random numbers
    for _ in range(500):
        val = random.randint(1, 1000)
        ll.append(val)
        added_values.append(val)

    print(f"Added {ll.length()} random numbers")

    # Verify all values are present
    missing = []
    for val in added_values:
        if not ll.search(val):
            missing.append(val)

    print(f"Missing values: {len(missing)}")

    # Random deletions
    deletions = 0
    for _ in range(100):
        if added_values:
            val_to_delete = random.choice(added_values)
            if ll.delete(val_to_delete):
                deletions += 1
                added_values.remove(val_to_delete)

    print(f"Successful deletions: {deletions}")
    print(f"Remaining length: {ll.length()}")

    # Test reverse
    ll.reverse()
    print("Stress test completed successfully!")


def edge_case_tests():
    print("=== Edge Case Tests ===")

    # Test 1: Single node operations
    ll = LinkedList()
    ll.append(1)
    print("Single node list:")
    ll.print_list()
    ll.reverse()
    print("After reverse:")
    ll.print_list()
    print()

    # Test 2: Two nodes
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(2)
    print("Two nodes:")
    ll2.print_list()
    ll2.reverse()
    print("After reverse:")
    ll2.print_list()
    print()

    # Test 3: Delete until empty
    ll3 = LinkedList()
    for i in range(5):
        ll3.append(i)

    print("Delete until empty:")
    ll3.print_list()
    while not ll3.is_empty():
        ll3.delete(ll3.head.data)  # type: ignore
        ll3.print_list()
    print()


if __name__ == "__main__":
    comprehensive_test()
    print("\n" + "=" * 50 + "\n")
    stress_test()
    print("\n" + "=" * 50 + "\n")
    edge_case_tests()
    # performance_test()  # Uncomment for performance testing
