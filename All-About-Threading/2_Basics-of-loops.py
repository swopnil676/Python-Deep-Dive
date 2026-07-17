import threading
import time

def count(n):
    for i in range(1, n+1):
        print(f"{threading.current_thread().name}: {i}")
        time.sleep(0.01)

for i in range(2):
    x = threading.Thread(target=count, args=(10,), name=f"Thread-{i+1}")
    x.start()

print("Main Thread Finished")