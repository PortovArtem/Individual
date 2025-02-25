import random

def generate_random_list(count, min_val=5, max_val=1000):
    """√енерирует список случайных чисел в заданном диапазоне."""
    return [random.randint(min_val, max_val) for _ in range(count)]

if __name__ == "__main__":
    count = 10 + 10  # 10 (є по списку) + 10
    random_numbers = generate_random_list(count)

    print("—генерированные числа:")
    print(random_numbers)
