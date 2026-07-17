import threading
import time

def count1(n):
    for i in range(1, n+1):
        print(f"{threading.current_thread().name}: {i}")
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        print(f"{threading.current_thread().name}: {i}")
        time.sleep(0.01)


x = threading.Thread(target=count1, args=(10,), name="Thread-1")
x.start()

x = threading.Thread(target=count2, args=(10,), name="Thread-2")
x.start()

print("Main Thread Finished")