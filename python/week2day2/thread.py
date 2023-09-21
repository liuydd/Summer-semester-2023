import threading
from threading import Thread
import time

lock = threading.Lock()

l = []
def thread_func(id, instructions):
    global l
    for inst in instructions:
        time.sleep(0.1)
        if inst.values() == 1:
            lock.acquire(blocking=True)
        elif inst.values() == -1:
            lock.release()
        elif inst.values() == 0:
            l.append(id)
            print(l)
    return

instructions = []
num_threads, num_instructions = map(int, input().split(' '))
for i in range(num_instructions):
    instructions.append([item for item in map(int, input().split(' '))])

threads = []
for id in range(num_threads):
    thread = Thread(target=thread_func, args=(id, instructions))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
