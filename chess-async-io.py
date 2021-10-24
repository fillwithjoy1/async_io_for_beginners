import asyncio
import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 32
move_pairs = 30


async def main(x):
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        time.sleep(my_compute_time)
        print(f"Waiting on opponent on board {x}.")
        await asyncio.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


async def async_io():
    tasks = []
    for i in range(opponents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")
