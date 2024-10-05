import asyncio

# A shared variable

shared_resource =0

# An asyncio Lck
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f'Resources before modification {shared_resource}')
        shared_resource +=1 # Modify the shared resources
        await asyncio.sleep(1) # Simulating networkor IO operation
        print(f'Resorces after modification {shared_resource}')
        # Critical section ends


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())