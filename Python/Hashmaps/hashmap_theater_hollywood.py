# hashmap_theater_hollywood.py
import time
import random
import string
from hash_map import HashTable

# CONFIG
START_CAPACITY = 20
TOTAL_INSERTS = 2000
STEP_DELAY = 0.02
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


def rand_key(length=6):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def progress_bar(current, total, width=BAR_WIDTH):
    filled = int((current / total) * width)
    percentage = (current / total) * 100
    return f"{GREEN}[{'█' * filled}{'░' * (width - filled)}]{RESET} {percentage:.1f}%"


def clear_screen():
    print("\033[2J\033[H", end="")


def bucket_lengths(table):
    lens = []
    for bucket in table.bucket_array:
        count = 0
        if bucket:
            node = bucket.head
            while node:
                count += 1
                node = node.next
        lens.append(count)
    return lens


def histogram(lens, max_display=12, max_bar_width=40):
    """Enhanced histogram with scaling for better visualization"""
    histo = []
    max_count = max((lens.count(i) for i in range(max_display)), default=1)

    for i in range(max_display):
        count = lens.count(i)
        if count > 0:
            # Scale bars relative to max count
            bar_len = int((count / max_count) * max_bar_width)
            bar = "█" * bar_len

            # Color code by severity
            if i >= 8:
                color = RED
            elif i >= 5:
                color = YELLOW
            else:
                color = CYAN

            histo.append(
                f"{color}Chain {i:2d}: {bar} {RESET}{DIM}({count} buckets){RESET}"
            )

    return "\n".join(histo) if histo else f"{DIM}No chains yet...{RESET}"


def dramatic_warning(longest, prev_longest):
    """Enhanced warnings with progression tracking"""
    if longest > prev_longest and longest >= 5:
        if longest >= 12:
            return (
                f"{RED}{BOLD}☠️☠️☠️ CATASTROPHIC CHAIN COLLAPSE! len={longest} ☠️☠️☠️{RESET}"
            )
        if longest >= 10:
            return (
                f"{RED}{BOLD}☠️ CHAINS HAVE BREACHED CONTAINMENT! len={longest}{RESET}"
            )
        if longest >= 7:
            return f"{MAGENTA}{BOLD}⚠️ CHAIN MONSTER DETECTED len={longest}!{RESET}"
        if longest >= 5:
            return f"{YELLOW}⚡ Chains Rising… len={longest}{RESET}"
    return None


def calculate_stats(lens):
    """Calculate distribution statistics"""
    if not lens:
        return 0, 0, 0

    non_empty = [l for l in lens if l > 0]
    avg_chain = sum(non_empty) / len(non_empty) if non_empty else 0
    collisions = sum(1 for l in lens if l > 1)
    empty_buckets = lens.count(0)

    return avg_chain, collisions, empty_buckets


def hollywood_mode(total_inserts=TOTAL_INSERTS, step_delay=STEP_DELAY):
    table = HashTable(START_CAPACITY)
    last_capacity = table.capacity
    rehash_count = 0
    max_chain_ever = 0
    prev_longest = 0
    rehash_moments = []

    # Opening sequence
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(
        f"{BOLD}{CYAN}🎬 HASHMAP: RISE OF THE CHAINS — A Data Structure Thriller{RESET}"
    )
    print(f"{BOLD}{CYAN}{'='*60}{RESET}\n")
    print(f"{DIM}Starring: Your Custom Hash Table Implementation{RESET}")
    print(f"{DIM}Featuring: {total_inserts} random insertions{RESET}\n")
    time.sleep(1.2)

    start = time.time()

    for i in range(1, total_inserts + 1):
        key = rand_key()
        table.put(key, i)

        # Only update display every few iterations for performance
        if i % 5 == 0 or i == total_inserts:
            clear_screen()

            lens = bucket_lengths(table)
            longest = max(lens) if lens else 0
            max_chain_ever = max(max_chain_ever, longest)
            load = table.size / table.capacity
            avg_chain, collisions, empty = calculate_stats(lens)

            # Header
            print(f"{BOLD}{CYAN}🎬 HASHMAP: RISE OF THE CHAINS{RESET}")
            print(
                progress_bar(i, total_inserts) + f"  Inserts: {i:,}/{total_inserts:,}"
            )
            print()

            # Core Metrics
            print(f"{BOLD}📊 CORE METRICS{RESET}")
            print(f"  📦 Items Stored:    {table.size:,}")
            print(f"  🏛️  Bucket Capacity: {table.capacity:,}")
            print(f"  📉 Load Factor:     {load:.3f} {'🔥' if load >= 0.75 else ''}")
            print(f"  🔗 Longest Chain:   {longest} {'⚠️' if longest >= 5 else '✓'}")
            print(f"  📊 Avg Chain (≠0):  {avg_chain:.2f}")
            print(f"  💥 Collision Zones: {collisions}")
            print(f"  ⚪ Empty Buckets:   {empty}")
            print()

            # Rehash Drama
            if table.capacity != last_capacity:
                rehash_count += 1
                rehash_moments.append((i, last_capacity, table.capacity))
                print(f"{YELLOW}{BOLD}🚨 REHASH EVENT #{rehash_count}!{RESET}")
                print(
                    f"{YELLOW}   Expanded: {last_capacity} → {table.capacity} buckets{RESET}"
                )
                print(f"{YELLOW}   Redistributing all {table.size} items...{RESET}")
                print()
                last_capacity = table.capacity

            # Chain threat alerts
            warn = dramatic_warning(longest, prev_longest)
            if warn:
                print(warn)
                print()
            prev_longest = longest

            # Histogram
            print(f"{BOLD}📈 BUCKET DISTRIBUTION{RESET}")
            print(histogram(lens))

            time.sleep(step_delay)

    end = time.time()

    # Final Statistics Screen
    clear_screen()
    final_lens = bucket_lengths(table)
    final_avg, final_collisions, final_empty = calculate_stats(final_lens)

    print(f"\n{BOLD}{GREEN}{'='*60}{RESET}")
    print(f"{BOLD}{GREEN}✅ MISSION COMPLETE — THE CHAINS HAVE BEEN TAMED!{RESET}")
    print(f"{BOLD}{GREEN}{'='*60}{RESET}\n")

    print(f"{BOLD}🎭 FINAL STATISTICS{RESET}")
    print(f"  ⏱️  Runtime:           {end - start:.2f} seconds")
    print(f"  ⚡ Ops/second:        {total_inserts / (end - start):.0f}")
    print(f"  📦 Total Items:       {table.size:,}")
    print(f"  🏛️  Final Capacity:    {table.capacity:,}")
    print(f"  📉 Final Load:        {table.size / table.capacity:.3f}")
    print(f"  🔄 Rehash Events:     {rehash_count}")
    print(f"  🔗 Max Chain Length:  {max_chain_ever}")
    print(f"  📊 Avg Chain (≠0):    {final_avg:.2f}")
    print(f"  💥 Final Collisions:  {final_collisions}")
    print(f"  ⚪ Empty Buckets:     {final_empty}/{table.capacity}")

    if rehash_moments:
        print(f"\n{BOLD}🚨 REHASH TIMELINE{RESET}")
        for idx, (insert_num, old_cap, new_cap) in enumerate(rehash_moments, 1):
            print(f"  #{idx} @ insert {insert_num:,}: {old_cap} → {new_cap} buckets")

    print(f"\n{BOLD}🎯 PERFORMANCE ANALYSIS{RESET}")
    efficiency = (1 - final_collisions / table.size) * 100 if table.size > 0 else 100
    print(f"  Distribution Efficiency: {efficiency:.1f}%")

    if final_avg < 2:
        print(f"  {GREEN}✓ Excellent distribution! Average chain < 2{RESET}")
    elif final_avg < 3:
        print(f"  {YELLOW}○ Good distribution. Average chain < 3{RESET}")
    else:
        print(f"  {RED}⚠ High collision rate. Consider tuning hash function{RESET}")

    print(f"\n{MAGENTA}{BOLD}🎬 Thanks for watching the chaos unravel.{RESET}")
    print(
        f"{DIM}Hash tables: Turning O(n) searches into O(1) magic since 1953.{RESET}\n"
    )


if __name__ == "__main__":
    import sys

    # Allow custom parameters from command line
    total = int(sys.argv[1]) if len(sys.argv) > 1 else TOTAL_INSERTS
    delay = float(sys.argv[2]) if len(sys.argv) > 2 else STEP_DELAY

    hollywood_mode(total_inserts=total, step_delay=delay)
