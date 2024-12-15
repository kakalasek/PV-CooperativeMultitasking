import asyncio
import time
import sys

async def print_time():
    while True:
        print(time.ctime())
        await asyncio.sleep(5)

def echo_input():
    print(input().upper())

async def main():
    asyncio.get_event_loop().add_reader(
        sys.stdin,
        echo_input
    )
    await print_time()

if __name__ == "__main__":
    asyncio.run(main())