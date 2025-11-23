from typing import Optional
import time

class LinearDatabase:
    def __init__(self, filename="test_data.csv") -> None:
        self.filename = filename

    def find(self, target_id: int) -> Optional[dict]:
        """Linear search through file for record with target_id"""
        with open(self.filename, 'r') as f:
            next(f)  # Skip header
            for line in f:
                record = line.strip().split(',')
                record_id = int(record[0])
                if record_id == target_id:
                    return {
                        'name': record[1],
                        'email': record[2],
                        'age': record[3]
                    }
        return None

if __name__ == "__main__":
    db = LinearDatabase()
    
    # Test different positions to see performance
    test_ids = [1, 500000, 999999, 1000001]
    
    for target_id in test_ids:
        print(f"\n=== Searching for record #{target_id} ===")
        start = time.time()
        result = db.find(target_id)
        end = time.time()
        
        if result:
            print(f"Record found: {result}")
        else:
            print("Record not found.")
        print(f"Search took: {end - start:.4f} seconds")