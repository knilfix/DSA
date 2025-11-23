from typing import Optional

class HashmapDatabase:
    """In-memory hashmap: {id -> file_position}"""

    def __init__(self, filename="test_data.csv") -> None:
        self.filename = filename
        self.index = {}  # {int: int} mapping
        self._build_index()

    def _build_index(self) -> None:
        """Build the in-memory index mapping IDs to file positions"""
        with open(self.filename, 'r') as f:
            f.readline()  # Skip header

            while True:
                position = f.tell()
                line = f.readline()

                if not line:
                    break

                key = int(line.strip().split(',')[0])  # Convert to int
                self.index[key] = position
        print(f"Index built: {len(self.index)} entries in memory")

    def find(self, target_key: int) -> Optional[dict]:  # Accept int
        """Direct lookups with integer keys"""
        position = self.index.get(target_key)  # Integer lookup

        if position is None:
            return None
            
        with open(self.filename, 'r') as f:
            f.seek(position)
            record = f.readline().strip().split(',')
            return {
                "name": record[1],
                "email": record[2],
                "age": record[3],
            }

if __name__ == "__main__":
    import time
    
    # Build the index (one-time cost)
    print("Building index...")
    start_build = time.time()
    db = HashmapDatabase()
    end_build = time.time()
    print(f"Index build time: {end_build - start_build:.4f} seconds\n")
    
    # Test searches (should be super fast now!)
    test_keys = [1, 500000, 999999, 1000001]
    
    for key in test_keys:
        print(f"=== Searching for record #{key} ===")
        start = time.time()
        result = db.find(key)
        end = time.time()
        
        if result:
            print(f"Record found: {result}")
        else:
            print("Record not found.")
        print(f"Search took: {end - start:.4f} seconds\n")