import time
from typing import Optional, List, Dict, Any

class DatabaseTester:
    def __init__(self):
        self.test_keys = [1, 500000, 999999, 1000001]
        self.results = {}
    
    def run_tests(self, database_instance, database_name: str):
        """Run standardized tests on any database instance"""
        print(f"\n{'='*50}")
        print(f"Testing: {database_name}")
        print(f"{'='*50}")
        
        database_results = {
            'name': database_name,
            'searches': {},
            'total_time': 0
        }
        
        for key in self.test_keys:
            print(f"\n--- Searching for record #{key} ---")
            start = time.time()
            result = database_instance.find(key)  # Convert to string for hashmap
            end = time.time()
            search_time = end - start
            
            database_results['searches'][key] = {
                'time': search_time,
                'found': result is not None,
                'data': result
            }
            database_results['total_time'] += search_time
            
            if result:
                print(f"Record found: {result}")
            else:
                print("Record not found.")
            print(f"Search took: {search_time:.4f} seconds")
        
        self.results[database_name] = database_results
        return database_results
    
    def print_comparison(self):
        """Print comparison of all tested databases"""
        print(f"\n{'='*60}")
        print(f"PERFORMANCE COMPARISON")
        print(f"{'='*60}")
        
        for db_name, results in self.results.items():
            print(f"\n{db_name}:")
            print(f"  Total search time: {results['total_time']:.4f}s")
            for key, search in results['searches'].items():
                status = "FOUND" if search['found'] else "NOT FOUND"
                print(f"    Key {key}: {search['time']:.4f}s ({status})")


# Usage example:
if __name__ == "__main__":
    from linear_database import LinearDatabase
    from hashmap_database import HashmapDatabase  
    
    tester = DatabaseTester()
    
    # Test Naive Database
    naive_db = LinearDatabase()
    tester.run_tests(naive_db, "Linear Database")  # Changed name to match class
    
    # Test Hashmap Database (include index build time)
    print(f"\nBuilding Hashmap Index...")
    start_build = time.time()
    hashmap_db = HashmapDatabase()
    build_time = time.time() - start_build
    print(f"Index build time: {build_time:.4f}s")
    
    tester.run_tests(hashmap_db, "Hashmap Database")
    
    # Add build time to hashmap total for fair comparison
    tester.results["Hashmap Database"]['build_time'] = build_time
    tester.results["Hashmap Database"]['total_time_with_build'] = (
        tester.results["Hashmap Database"]['total_time'] + build_time
    )
    
    # Print final comparison
    tester.print_comparison()
    
    # Show build time consideration
    print(f"\n{'='*60}")
    print(f"WITH INDEX BUILD TIME CONSIDERED:")
    print(f"{'='*60}")
    for db_name, results in tester.results.items():
        if 'build_time' in results:
            print(f"{db_name}: {results['total_time_with_build']:.4f}s (includes {results['build_time']:.4f}s build)")
        else:
            print(f"{db_name}: {results['total_time']:.4f}s")