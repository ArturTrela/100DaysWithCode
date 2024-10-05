import asyncio

async def fetch_data(id, sleep_time):
    print(f'Coroutine {id} starting fetch data')
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
#   Return some data as result
    return {"id": id, "data":f'Sample data from coroutine {id}'}


async def main():
#      Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1,2),fetch_data(2,3),fetch_data(3,1))
    for result in results:
        print(f'Received results {result}')

# Run the main coroutine
asyncio.run(main())