import time
import asyncio


# We add async to our function to declare it as a async-io function.
async def main(x):
    print(f"Starting Task {x}")
    # Here we use asyncio.sleep as it's non-blocking and allowing the program to check on the other main() functions.
    await asyncio.sleep(3)
    print(f"Finished Task {x}")


# Same declaration of async functions
async def async_io():
    # Here we create a list that tracks all the async tasks to-do.
    tasks = []
    for i in range(10):
        # Here we add the task of main() function 10 times and add it to the tasks list. Notice that the main is
        # wrapped in []
        tasks += [main(i)]
    # Finally, asyncio gathers the result of all the tasks in the task list. Notice the * asterisk
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.perf_counter()
    # This executes the async_io function as a asynchronous function from a non-async function.
    # Yes the if condition above executes as a non-async function.
    asyncio.run(async_io())
    print(f"Took {time.perf_counter() - start_time} secs")
