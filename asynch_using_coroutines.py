import asyncio

async def coroutine1():
    print("Coroutine 1 started")
    await asyncio.sleep(1)
    print("Coroutine 1 ended")

async def coroutine2():
    print("Coroutine 2 started")
    await asyncio.sleep(2)
    print("Coroutine 2 ended")

async def main():
    await asyncio.gather(coroutine1(), coroutine2())

asyncio.run(main())
#In this example, we define two coroutines: coroutine1() and coroutine2(). 
# Each of these coroutines prints a message, sleeps for a specified amount of time using 
# the asyncio.sleep() function, and then prints another message. 
# The main() function uses the asyncio.gather()
#  function to run both coroutines concurrently.

#The asyncio.run() function runs the event loop until all tasks are completed.
#  During the execution of the program, the coroutines are paused and 
# resumed as needed to allow other code to run concurrentl