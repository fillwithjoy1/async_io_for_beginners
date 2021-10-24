import time
import asyncio


async def main(x):
    print(f"Starting Task {x}")
    await asyncio.sleep(3)
    print(f"Finished Task {x}")


async def async_io():
    tasks = []
    for i in range(10):
        tasks += [main(i)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Took {time.perf_counter() - start_time} secs")
