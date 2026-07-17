import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.") # Simulate a network or IO operation
    await asyncio.sleep(sleep_time)
    # Return some data as a result
    return {"id": id, "data":f"Sample data from coroutine {id}"}


async def main():
    print("Start of main coroutine\n")

    # Run coroutines concurrently and gather their return values
    results  = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))
    
    # Process the results
    for result in results:
        print(f"Received result: {result}")

    print("\nEnd of main coroutine")

# Run the main coroutine
asyncio.run(main())