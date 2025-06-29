# INTI Matriculation Number: P23015051
# Name: Ng Jing Wen

import threading
import time
import random

# Part 1: Discussion of Multithreading (In Report)


# Part 2: Generate 100 Random Numbers
def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]


# Part 3: Multithreaded Execution
def multithreaded_generation():
    rounds = 10
    results = []

    for round_num in range(rounds):
        threads = []
        numbers_sets = []

        start_time = time.time_ns()

        # Thread target function
        def thread_task():
            numbers_sets.append(generate_random_numbers())

        # Create and start 3 threads
        for _ in range(3):
            t = threading.Thread(target=thread_task)
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        end_time = time.time_ns()
        elapsed = end_time - start_time
        results.append(elapsed)

        print(f"Round {round_num + 1}: {elapsed} ns")

    avg_time = sum(results) / rounds
    print(f"\nAverage Time (Multithreaded): {avg_time:.2f} ns")
    return results


# Part 4: Non-Multithreaded Execution
def non_multithreaded_generation():
    rounds = 10
    results = []

    for round_num in range(rounds):
        start_time = time.time_ns()

        # Generate 3 sets in sequence
        for _ in range(3):
            _ = generate_random_numbers()

        end_time = time.time_ns()
        elapsed = end_time - start_time
        results.append(elapsed)

        print(f"Round {round_num + 1}: {elapsed} ns")

    avg_time = sum(results) / rounds
    print(f"\nAverage Time (Non-Multithreaded): {avg_time:.2f} ns")
    return results


def main():
    print("Round-by-Round Performance Comparison:")
    # Running Multithreaded Generation...
    multi_times = []
    for _ in range(10):
        start = time.time_ns()
        threads = []
        result = []

        def task():
            result.append(generate_random_numbers())

        for _ in range(3):
            t = threading.Thread(target=task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        end = time.time_ns()
        multi_times.append(end - start)

    # Running Non-Multithreaded Generation...
    non_multi_times = []
    for _ in range(10):
        start = time.time_ns()
        for _ in range(3):
            _ = generate_random_numbers()
        end = time.time_ns()
        non_multi_times.append(end - start)

    # Header for per-round time table
    print("------|---------------------------|-------------------------------|-----------------")
    print("Round | Multithreading Time (ns)  | Non-Multithreading Time (ns)  | Difference (ns)")
    print("------|---------------------------|-------------------------------|-----------------")
    for i in range(10):
        diff = abs(multi_times[i] - non_multi_times[i])
        print(f"{i + 1:>5} | {multi_times[i]:>25} | {non_multi_times[i]:>29} | {diff:>15}")
    print("------|---------------------------|-------------------------------|-----------------")

    total_multi = sum(multi_times)
    total_non_multi = sum(non_multi_times)
    total_diff = abs(total_multi - total_non_multi)
    avg_multi = total_multi / 10
    avg_non_multi = total_non_multi / 10
    avg_diff = abs(avg_multi - avg_non_multi)

    print("\nSummary of Results:")
    # Header for metric table
    print("-------------|----------------------|--------------------------|-----------------")
    print("Metric       | Multithreading (ns)  | Non-Multithreading (ns)  | Difference (ns)")
    print("-------------|----------------------|--------------------------|-----------------")
    print(f"Total Time   | {total_multi:>20} | {total_non_multi:>24} | {total_diff:>15}")
    print(f"Average Time | {avg_multi:>20.2f} | {avg_non_multi:>24.2f} | {avg_diff:>15.2f}")
    print("-------------|----------------------|--------------------------|-----------------")


if __name__ == "__main__":
    main()