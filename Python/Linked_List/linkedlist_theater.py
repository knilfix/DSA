# linkedlist_theater.py
import time
import random
import string
from linked_list import LinkedList

# CONFIG
TOTAL_OPERATIONS = 500
STEP_DELAY = 0.03
BAR_WIDTH = 35

# ANSI Colors
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def rand_data():
    """Generate random data"""
    return random.randint(1, 999)


def progress_bar(current, total, width=BAR_WIDTH):
    filled = int((current / total) * width)
    percentage = (current / total) * 100
    return f"{GREEN}[{'█' * filled}{'░' * (width - filled)}]{RESET} {percentage:.1f}%"


def clear_screen():
    print("\033[2J\033[H", end="")


def visualize_list(linked_list, max_display=20):
    """Create a visual representation of the linked list"""
    if linked_list.is_empty():
        return f"{DIM}[empty]{RESET}"

    elements = []
    current = linked_list.head
    count = 0

    while current and count < max_display:
        elements.append(str(current.data))
        current = current.next_node
        count += 1

    if current:  # More elements exist
        elements.append("...")

    visualization = f"{CYAN}HEAD{RESET} → " + " → ".join(elements)

    if not current:  # We reached the end
        visualization += f" → {DIM}NULL{RESET}"

    return visualization


def operation_description(op_type, data=None, target=None):
    """Generate dramatic descriptions for operations"""
    descriptions = {
        "prepend": f"{CYAN}⬅️  PREPEND{RESET} {BOLD}{data}{RESET} to beginning",
        "append": f"{GREEN}➡️  APPEND{RESET} {BOLD}{data}{RESET} to end",
        "insert": f"{YELLOW}📌 INSERT{RESET} {BOLD}{data}{RESET} after {target}",
        "delete": f"{RED}❌ DELETE{RESET} {BOLD}{data}{RESET}",
        "search": f"{BLUE}🔍 SEARCH{RESET} for {BOLD}{data}{RESET}",
        "reverse": f"{MAGENTA}🔄 REVERSE{RESET} entire list",
    }
    return descriptions.get(op_type, f"Unknown operation: {op_type}")


def dramatic_warning(size, search_time=None):
    """Provide warnings about performance"""
    if search_time and search_time > 0.001:
        return f"{RED}{BOLD}⚠️  SLOW SEARCH DETECTED! O(n) traversal took {search_time*1000:.2f}ms{RESET}"

    if size >= 200:
        return f"{YELLOW}⚡ List growing long... Traversals getting expensive! (size={size}){RESET}"

    if size >= 100:
        return f"{YELLOW}⚠️  Performance degrading with size={size}{RESET}"

    return None


def hollywood_mode(total_ops=TOTAL_OPERATIONS, step_delay=STEP_DELAY):
    ll = LinkedList()

    # Statistics tracking
    prepend_count = 0
    append_count = 0
    insert_count = 0
    delete_count = 0
    search_count = 0
    reverse_count = 0

    failed_operations = 0
    total_search_time = 0
    max_search_time = 0

    # Opening sequence
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}🎬 LINKED LIST: THE GREAT TRAVERSAL{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}\n")
    print(f"{DIM}Witness the linear journey of pointer-chasing glory{RESET}")
    print(f"{DIM}Featuring: {total_ops} dramatic operations{RESET}\n")
    time.sleep(1.2)

    start = time.time()

    for i in range(1, total_ops + 1):
        # Choose random operation
        if ll.is_empty():
            op = random.choice(["prepend", "append"])
        else:
            op = random.choice(
                ["prepend", "append", "insert", "delete", "search", "reverse"]
            )

        data = rand_data()
        current_op_desc = ""
        search_time_this_op = None

        # Perform operation
        if op == "prepend":
            ll.prepend(data)
            prepend_count += 1
            current_op_desc = operation_description("prepend", data)

        elif op == "append":
            ll.append(data)
            append_count += 1
            current_op_desc = operation_description("append", data)

        elif op == "insert":
            if ll.size > 0:
                target_idx = random.randint(0, ll.size - 1)
                target = ll.get(target_idx)
                ll.insert_after(target, data)
                insert_count += 1
                current_op_desc = operation_description("insert", data, target)
            else:
                ll.prepend(data)
                prepend_count += 1
                current_op_desc = operation_description("prepend", data)

        elif op == "delete":
            if ll.size > 0:
                target_idx = random.randint(0, ll.size - 1)
                target = ll.get(target_idx)
                success = ll.delete(target)
                if success:
                    delete_count += 1
                    current_op_desc = operation_description("delete", target)
                else:
                    failed_operations += 1
                    current_op_desc = f"{RED}❌ DELETE FAILED{RESET}"
            else:
                failed_operations += 1
                current_op_desc = f"{RED}❌ DELETE FAILED (empty list){RESET}"

        elif op == "search":
            search_target = rand_data()
            search_start = time.time()
            found = ll.search(search_target)
            search_end = time.time()
            search_time_this_op = search_end - search_start

            total_search_time += search_time_this_op
            max_search_time = max(max_search_time, search_time_this_op)

            search_count += 1
            status = f"{GREEN}FOUND{RESET}" if found else f"{RED}NOT FOUND{RESET}"
            current_op_desc = (
                f"{BLUE}🔍 SEARCH{RESET} for {BOLD}{search_target}{RESET} → {status}"
            )

        elif op == "reverse":
            ll.reverse()
            reverse_count += 1
            current_op_desc = operation_description("reverse")

        # Update display
        if i % 3 == 0 or i == total_ops:  # Update every 3 ops for performance
            clear_screen()

            # Header
            print(f"{BOLD}{CYAN}🎬 LINKED LIST: THE GREAT TRAVERSAL{RESET}")
            print(progress_bar(i, total_ops) + f"  Operations: {i:,}/{total_ops:,}")
            print()

            # Current operation
            print(f"{BOLD}🎬 CURRENT ACTION{RESET}")
            print(f"  {current_op_desc}")
            print()

            # Core metrics
            print(f"{BOLD}📊 LIST STATE{RESET}")
            print(f"  📏 Size: {ll.size:,} nodes")
            print(f"  🔗 Structure: Singly-linked")
            print()

            # Operation counts
            print(f"{BOLD}📈 OPERATION STATS{RESET}")
            print(f"  ⬅️  Prepends:  {prepend_count:,} {GREEN}(O(1)){RESET}")
            print(f"  ➡️  Appends:   {append_count:,} {YELLOW}(O(n)){RESET}")
            print(f"  📌 Inserts:   {insert_count:,} {YELLOW}(O(n)){RESET}")
            print(f"  ❌ Deletes:   {delete_count:,} {YELLOW}(O(n)){RESET}")
            print(f"  🔍 Searches:  {search_count:,} {RED}(O(n)){RESET}")
            print(f"  🔄 Reverses:  {reverse_count:,} {YELLOW}(O(n)){RESET}")

            if failed_operations > 0:
                print(f"  {RED}⚠️  Failed ops: {failed_operations}{RESET}")
            print()

            # Search performance
            if search_count > 0:
                avg_search = total_search_time / search_count
                print(f"{BOLD}🔍 SEARCH PERFORMANCE{RESET}")
                print(f"  Average time: {avg_search*1000:.3f}ms per search")
                print(f"  Slowest search: {max_search_time*1000:.3f}ms")
                print()

            # Performance warnings
            warn = dramatic_warning(ll.size, search_time_this_op)
            if warn:
                print(warn)
                print()

            # Visual representation
            print(f"{BOLD}🔗 LIST VISUALIZATION{RESET}")
            print(f"  {visualize_list(ll)}")

            time.sleep(step_delay)

    end = time.time()

    # Final statistics
    clear_screen()
    print(f"\n{BOLD}{GREEN}{'='*60}{RESET}")
    print(f"{BOLD}{GREEN}✅ THE TRAVERSAL IS COMPLETE!{RESET}")
    print(f"{BOLD}{GREEN}{'='*60}{RESET}\n")

    print(f"{BOLD}🎭 FINAL STATISTICS{RESET}")
    print(f"  ⏱️  Runtime:        {end - start:.2f} seconds")
    print(f"  ⚡ Ops/second:     {total_ops / (end - start):.0f}")
    print(f"  📏 Final Size:     {ll.size:,} nodes")
    print(
        f"  🎯 Success Rate:   {((total_ops - failed_operations) / total_ops * 100):.1f}%"
    )
    print()

    print(f"{BOLD}📊 OPERATION BREAKDOWN{RESET}")
    print(f"  ⬅️  Prepends:  {prepend_count:,} {GREEN}← Fast! O(1){RESET}")
    print(f"  ➡️  Appends:   {append_count:,} {YELLOW}← Slow! O(n){RESET}")
    print(f"  📌 Inserts:   {insert_count:,} {YELLOW}← Slow! O(n){RESET}")
    print(f"  ❌ Deletes:   {delete_count:,} {YELLOW}← Slow! O(n){RESET}")
    print(f"  🔍 Searches:  {search_count:,} {RED}← Very Slow! O(n){RESET}")
    print(f"  🔄 Reverses:  {reverse_count:,} {YELLOW}← Slow! O(n){RESET}")
    print()

    if search_count > 0:
        avg_search = total_search_time / search_count
        print(f"{BOLD}🔍 SEARCH ANALYSIS{RESET}")
        print(f"  Total searches:    {search_count:,}")
        print(f"  Average time:      {avg_search*1000:.3f}ms")
        print(f"  Slowest search:    {max_search_time*1000:.3f}ms")
        print(f"  Total time spent:  {total_search_time:.3f}s")
        print()

    print(f"{BOLD}🎯 PERFORMANCE INSIGHTS{RESET}")

    # Calculate percentage of O(1) operations
    o1_ops = prepend_count
    on_ops = append_count + insert_count + delete_count + search_count + reverse_count
    o1_percent = (o1_ops / total_ops * 100) if total_ops > 0 else 0

    print(f"  O(1) operations: {o1_percent:.1f}% (only prepends!)")
    print(f"  O(n) operations: {100 - o1_percent:.1f}% (everything else)")
    print()

    if ll.size > 50:
        print(
            f"  {YELLOW}⚠️  With {ll.size} nodes, most operations require traversal{RESET}"
        )
        print(f"  {YELLOW}⚠️  Consider using a hash table for O(1) lookups!{RESET}")
    else:
        print(f"  {GREEN}✓ List size reasonable for sequential access{RESET}")

    print(f"\n{BOLD}🔗 FINAL LIST STATE{RESET}")
    print(f"  {visualize_list(ll, max_display=30)}")

    print(f"\n{MAGENTA}{BOLD}🎬 The pointer-chasing saga concludes.{RESET}")
    print(f"{DIM}Linked Lists: Great for insertion, terrible for search.{RESET}")
    print(
        f"{DIM}Hash Tables: Great for search, terrible for... waiting, nothing!{RESET}\n"
    )


if __name__ == "__main__":
    import sys

    # Allow custom parameters
    total = int(sys.argv[1]) if len(sys.argv) > 1 else TOTAL_OPERATIONS
    delay = float(sys.argv[2]) if len(sys.argv) > 2 else STEP_DELAY

    hollywood_mode(total_ops=total, step_delay=delay)
