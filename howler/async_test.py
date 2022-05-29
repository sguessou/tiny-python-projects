import asyncio
import os
import threading
import multiprocessing


async def coroutine_add_one(number: int) -> int:
    return number + 1


result = asyncio.run(coroutine_add_one(1))

print(result)

print(f"python process running with process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"python is currently running {total_threads} thread(s)")
print(f"the current thread is {thread_name}")


def hello_from_process():
    print(f"hello from child process {os.getpid()}!")


if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"hello from parent process {os.getpid()}")

    hello_process.join()
