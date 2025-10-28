# hashmap_live_theater.py
import time
import random
import string
from hash_map import HashTable  # import your class as implemented earlier

# CONFIG
START_CAPACITY = 20
TOTAL_INSERTS = 5000
STEP_DELAY = 0.01  # seconds between screen refreshes
BAR_WIDTH = 30


def rand_key(length=6):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def progress_bar(current, total, width=BAR_WIDTH):
    filled = int((current / total) * width)
    return f"[{'█' * filled}{'░' * (width - filled)}]"


def clear_screen():
    print("\033[2J\033[H", end="")  # ANSI: clear + move cursor to home


def bucket_lengths(table):
    lens = []
    for bucket in table.bucket_array:
        count = 0
        if bucket:
            current = bucket.head
            while current:
                count += 1
                current = current.next
        lens.append(count)
    return lens


def hashmap_live_show(total_inserts=TOTAL_INSERTS, step_delay=STEP_DELAY):
    table = HashTable(START_CAPACITY)  # use your constructor signature
    last_capacity = table.capacity

    print("🎬 Welcome to HashMap Live Theater!")
    time.sleep(0.7)

    start = time.time()
    for i in range(1, total_inserts + 1):
        key = rand_key()
        value = i
        table.put(key, value)  # use put() as in your implementation

        # redraw every iteration (you can change to i % N == 0 to reduce flicker)
        clear_screen()

        load = table.size / table.capacity
        lengths = bucket_lengths(table)
        longest = max(lengths) if lengths else 0
        avg_chain = sum(lengths) / len(lengths) if lengths else 0.0

        bar = progress_bar(i, total_inserts)

        # flash a rehash banner when capacity changed
        if table.capacity != last_capacity:
            print("\033[1;33m🚨 REHASH TRIGGERED!\033[0m")  # yellow bold
            last_capacity = table.capacity

        print(f"🎬 HashMap Live Theater")
        print(bar + f"  Inserts: {i}/{total_inserts}")
        print(f"Size: {table.size}")
        print(f"Capacity: {table.capacity}")
        print(f"Load factor: {load:.2f}")
        print(f"Longest chain: {longest}")
        print(f"Avg chain: {avg_chain:.2f}")

        time.sleep(step_delay)

    end = time.time()
    print(f"\n✅ Complete! Total time: {end - start:.4f}s")


if __name__ == "__main__":
    hashmap_live_show()
