import csv
import random
import statistics
import time

from algorithms import (
    iterative_binary_search,
    recursive_binary_search,
    sequential_search,
)

DATA_SIZES = [5_000, 50_000, 100_000, 150_000, 1_000_000]
NUMBER_OF_TRIALS = 10

def verify_result(values, target, index):
    if index != -1:
        assert values[index] == target
    else:
        assert target not in values

def time_search(search_function):
    start_time = time.perf_counter()
    index = search_function()
    end_time = time.perf_counter()

    elapsed_microseconds = (end_time - start_time) * 1_000_000

    return index, elapsed_microseconds 


def test_data_size(size):
    recursive_times = []
    iterative_times = []
    sequential_times = []

    for trial in range(NUMBER_OF_TRIALS):
        values = sorted(
            random.randint(1, 1_000_000)
            for _ in range(size)
        )

        if random.random() < 0.5:
            target = random.choice(values)
        else:
            target = 1_000_001

        recursive_index, recursive_time = time_search(
            lambda: recursive_binary_search(
                values, target, 0, len(values) - 1
            )
        )

        iterative_index, iterative_time = time_search(
            lambda: iterative_binary_search(values, target)
        )

        sequential_index, sequential_time = time_search(
            lambda: sequential_search(values, target)
        )

        verify_result(values, target, recursive_index)
        verify_result(values, target, iterative_index)
        verify_result(values, target, sequential_index)

        recursive_times.append(recursive_time)
        iterative_times.append(iterative_time)
        sequential_times.append(sequential_time)

        print(f"Size {size:,} - Trial {trial + 1} complete")

    recursive_median = statistics.median(recursive_times)
    iterative_median = statistics.median(iterative_times)
    sequential_median = statistics.median(sequential_times)

    return (
        recursive_median,
        iterative_median,
        sequential_median,
    )


def save_results(results):
    file_path = "phase_3_runtime_analysis/results.csv"

    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow([
            "data_size",
            "recursive_binary_us",
            "iterative_binary_us",
            "sequential_us",
        ])

        writer.writerows(results)


def main():
    results = []

    for size in DATA_SIZES:
        print(f"\nTesting data size: {size:,}")

        recursive_median, iterative_median, sequential_median = (
            test_data_size(size)
        )

        results.append([
            size,
            recursive_median,
            iterative_median,
            sequential_median,
        ])

        print(f"Recursive Binary Median: {recursive_median:.3f} us")
        print(f"Iterative Binary Median: {iterative_median:.3f} us")
        print(f"Sequential Median: {sequential_median:.3f} us")

    save_results(results)

    print("\nRuntime analysis complete.")
    print("Results saved to results.csv")


if __name__ == "__main__":
    main()
