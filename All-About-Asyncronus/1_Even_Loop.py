import asyncio

# coroutine function
async def main():
    print("Start of main coroutine")

main()  # main() -> Coroutine object

# Run the main coroutine
asyncio.run(main())