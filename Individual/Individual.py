import random

def generate_random_list(count, min_val=5, max_val=1000):
    """Generate a list of random numbers within the specified range."""
    return [random.randint(min_val, max_val) for _ in range(count)]

count = 10 + 10  # 10 (number in the list) + 10
random_numbers = generate_random_list(count)

print("Generated numbers:")
print(random_numbers)

print("Generated numbers again:")
print(generate_random_list(20))