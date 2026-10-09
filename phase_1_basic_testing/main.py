from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)


def test_searches(values, target, test_name):
    values.sort()

    print(f"\n--- {test_name} ---")
    print("Values:", values)
    print("Target:", target)

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

    for algorithm_name, index in results:
        if index != -1:
            assert values[index] == target
            print(f"{algorithm_name}: Found, index = {index}")
        else:
            assert target not in values
            print(f"{algorithm_name}: Not Found, index = -1")



def main():

    
    # Middle element
    test_searches([3, 5, 8, 12, 14, 18, 21], 12, "Middle Element")

    # Absent target
    test_searches([3, 5, 8, 12, 14, 18, 21], 9, "Absent Target")


    # First element
    test_searches([3, 5, 8, 12, 14, 18, 21], 3, "First Element")

    # Last element
    test_searches([3, 5, 8, 12, 14, 18, 21], 21, "Last Element")

    # One-element list - present
    test_searches([10], 10, "One Element Present")

    # One-element list - absent
    test_searches([10], 5, "One Element Absent")

    # Empty list
    test_searches([], 5, "Empty List")

    # Duplicate values
    test_searches([3, 5, 5, 5, 8, 12], 5, "Duplicate Values")


if __name__ == "__main__":
    main()