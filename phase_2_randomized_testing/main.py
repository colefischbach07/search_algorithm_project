import random

from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)


def run_random_test():
    values = [random.randint(1, 100) for _ in range(20)]
    values.sort()

    if random.random() < 0.5:
        target = random.choice(values)
        expected_to_be_present = True
    else:
        target = 101
        expected_to_be_present = False

    recursive_index = recursive_binary_search(
        values, target, 0, len(values) - 1
    )
    iterative_index = iterative_binary_search(values, target)
    sequential_index = sequential_search(values, target)

    results = [
        ("Recursive Binary Search", recursive_index),
        ("Iterative Binary Search", iterative_index),
        ("Sequential Search", sequential_index),
    ]

    print("\nSorted List:", values)
    print("Target:", target)
    print("Expected to be present:", expected_to_be_present)

    for algorithm_name, index in results:
        if index != -1:
            assert values[index] == target
            print(f"{algorithm_name}: Found at index {index}")
        else:
            assert target not in values
            print(f"{algorithm_name}: Not Found")


def main():
    for _ in range(10):
        run_random_test()


if __name__ == "__main__":
    main()