# demo.py

from linked_list import LinkedList
from linkedlist_theater import hollywood_mode

if __name__ == "__main__":
    print("🎬 Quick Linked List Demo\n")

    ll = LinkedList()

    print("Prepending values...")
    ll.prepend(10)
    ll.prepend(20)
    ll.prepend(30)  # List: 30 -> 20 -> 10
    ll.print_list()

    print("\nAppending values...")
    ll.append(40)
    ll.append(50)  # List: 30 -> 20 -> 10 -> 40 -> 50
    ll.print_list()

    print("\nInsert 25 after 20")
    ll.insert_after(20, 25)  # List: 30 -> 20 -> 25 -> 10 -> 40 -> 50
    ll.print_list()

    print("\nDelete 10")
    ll.delete(10)  # List: 30 -> 20 -> 25 -> 40 -> 50
    ll.print_list()

    print("\nSearch for 25:", ll.search(25))
    print("Length of list:", ll.length())

    print("\nReverse list...")
    ll.reverse()
    ll.print_list()

    print("\n🎟️  Demo complete!")
    print("\nNow launching the full cinematic linked list experience...\n")

    hollywood_mode(total_ops=300, step_delay=0.02)  # You can tweak this
