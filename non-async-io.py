import time


def main(x):
    print(f"Starting task {x}")
    time.sleep(3)
    print(f"Finished task {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    for i in range(10):
        main(i)
    print(f"Took {time.perf_counter() - start_time} secs")