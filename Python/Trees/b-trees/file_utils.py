import os
from typing import Dict


def get_file_size(filename: str) -> str:
    """Get the storage size of the file in human-readable format"""
    try:
        size_bytes = os.path.getsize(filename)
        
        # Convert to human readable
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    except FileNotFoundError:
        return "File not found"
    
def get_record_count(filename: str) -> int:
    """Count the number of records in the CSV file (excluding header)"""
    try:
        with open(filename, 'r') as f:
            next(f)  # Skip header
            return sum(1 for line in f)
    except FileNotFoundError:
        return 0
    
def get_database_stats(filename: str) -> Dict:
    """Get comprehensive file statistics"""
    return {
        'filename': filename,
        'file_size': get_file_size(filename),
        'total_records': get_record_count(filename),
        'file_path': os.path.abspath(filename)
    }

# Simple usage example
if __name__ == "__main__":
    stats = get_database_stats("test_data.csv")
    for key, value in stats.items():
        print(f"{key}: {value}")