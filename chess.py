import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 32
move_pairs = 30


def main(x):
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    for i in range(opponents):
        main(i)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")
