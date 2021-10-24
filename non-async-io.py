import time


def main(x):
    print(f"Starting task {x}")
    # Here we are doing a task that takes 3 seconds to complete
    time.sleep(3)
    print(f"Finished task {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # We run this task 10 times.
    for i in range(10):
        main(i)
    print(f"Took {time.perf_counter() - start_time} secs")
