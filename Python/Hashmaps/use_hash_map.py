from hash_map import HashTable
import random
import string

# Create a larger hash table
dictionary = HashTable(50)  # Start with capacity 50


# Generate random test data
def generate_random_key():
    """Generate random keys of different types"""
    key_type = random.choice(["string", "integer", "float"])

    if key_type == "string":
        length = random.randint(3, 10)
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))
    elif key_type == "integer":
        return random.randint(1, 1000)
    else:  # float
        return round(random.uniform(1.0, 100.0), 2)


def generate_random_value():
    """Generate random values of different types"""
    value_type = random.choice(
        ["string", "integer", "float", "list", "boolean", "dict"]
    )

    if value_type == "string":
        length = random.randint(5, 15)
        return "".join(random.choices(string.ascii_letters + " ", k=length))
    elif value_type == "integer":
        return random.randint(1, 10000)
    elif value_type == "float":
        return round(random.uniform(1.0, 1000.0), 2)
    elif value_type == "list":
        return [random.randint(1, 100) for _ in range(random.randint(2, 5))]
    elif value_type == "boolean":
        return random.choice([True, False])
    else:  # dict
        return {f"key_{i}": random.randint(1, 100) for i in range(random.randint(1, 3))}


# Insert 100 random key-value pairs
print("Inserting 100 random key-value pairs...")
test_data = {}
for i in range(100):
    key = generate_random_key()
    value = generate_random_value()
    test_data[key] = value
    dictionary.put(key, value)

print(f"Inserted {dictionary.size} items")
print(f"Final capacity: {dictionary.capacity}")
print(f"Load factor: {dictionary.size / dictionary.capacity:.2f}")

# Print a sample of the table
print("\nSample of hash table contents:")
dictionary.print_table()

# Test retrieval - verify all inserted data can be retrieved correctly
print("\nTesting retrieval of all inserted items...")
successful_retrievals = 0
failed_retrievals = 0

for key, expected_value in test_data.items():
    retrieved_value = dictionary.get(key)
    if retrieved_value == expected_value:
        successful_retrievals += 1
    else:
        failed_retrievals += 1
        print(
            f"ERROR: Key '{key}' - Expected: {expected_value}, Got: {retrieved_value}"
        )

print(f"\nRetrieval test results:")
print(f"Successful: {successful_retrievals}")
print(f"Failed: {failed_retrievals}")
print(f"Accuracy: {(successful_retrievals/len(test_data))*100:.1f}%")

# Test updates
print("\nTesting updates...")
keys_to_update = random.sample(list(test_data.keys()), min(10, len(test_data)))
for key in keys_to_update:
    new_value = "UPDATED_" + str(test_data[key])
    dictionary.put(key, new_value)
    test_data[key] = new_value

# Verify updates worked
print("Verifying updates...")
update_success = 0
for key in keys_to_update:
    if dictionary.get(key) == test_data[key]:
        update_success += 1

print(f"Updates successful: {update_success}/{len(keys_to_update)}")

# Test removals
print("\nTesting removals...")
keys_to_remove = random.sample(list(test_data.keys()), min(15, len(test_data)))
removal_success = 0

for key in keys_to_remove:
    if dictionary.remove(key):
        removal_success += 1
        del test_data[key]  # Remove from our test data too

print(f"Removed {removal_success} items successfully")
print(f"New size: {dictionary.size}")
print(f"New load factor: {dictionary.size / dictionary.capacity:.2f}")

# Final verification
print("\nFinal verification...")
final_success = 0
for key, expected_value in test_data.items():
    if dictionary.get(key) == expected_value:
        final_success += 1

print(
    f"Final accuracy: {final_success}/{len(test_data)} ({(final_success/len(test_data))*100:.1f}%)"
)

# Test non-existent keys
print("\nTesting non-existent keys...")
non_existent_test = 0
for i in range(20):
    fake_key = f"non_existent_key_{i}"
    if dictionary.get(fake_key) is None:
        non_existent_test += 1

print(f"Correctly handled {non_existent_test}/20 non-existent keys")

# Performance test - time some operations
import time

print("\nPerformance test - timing 1000 retrievals...")
start_time = time.time()

test_keys = list(test_data.keys())[: min(1000, len(test_data))]
for key in test_keys:
    _ = dictionary.get(key)

end_time = time.time()
print(f"Time for 1000 retrievals: {(end_time - start_time)*1000:.2f} milliseconds")
print(
    f"Average retrieval time: {(end_time - start_time)*1000/len(test_keys):.4f} ms per operation"
)
