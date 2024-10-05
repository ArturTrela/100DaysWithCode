import asyncio

async def access_resources(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f'Accessing resources {resource_id}')
        await asyncio.sleep(1) #Simulate work with resource
        print(f'Releasing resource {resource_id}')

async def main():
    semaphore = asyncio.Semaphore(2) #Allow two concurrent access
    await asyncio.gather(*(access_resources(semaphore,i) for i in range(5)))

asyncio.run(main())