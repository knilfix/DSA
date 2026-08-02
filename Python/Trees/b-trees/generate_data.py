# generate_data.py - Creates realistic test data using Faker with better formatting
from faker import Faker
import random

def generate_test_data(num_records=100000, filename="data.csv"):
    """Generate a CSV with ID and realistic user data using Faker"""
    fake = Faker()
    
    with open(filename, 'w') as f:
        f.write("id,name,email,age\n")
        for i in range(1, num_records + 1):
            # Generate realistic data with better formatting
            first_name = fake.first_name()
            last_name = fake.last_name()
            name = f"{first_name} {last_name}"
            
            # Create email from the generated names (more realistic)
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            
            age = random.randint(18, 80)
            f.write(f"{i},{name},{email},{age}\n")
    
    print(f"Generated {num_records} records in {filename}")


if __name__ == "__main__":
    # Run this to create your data file
    generate_test_data()