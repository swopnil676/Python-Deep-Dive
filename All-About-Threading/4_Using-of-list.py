import threading
import time

ls = []

def count1(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)


x = threading.Thread(target=count1, args=(10,), name="Thread-1")
x.start()

y = threading.Thread(target=count2, args=(10,), name="Thread-2")
y.start()

# Threads syncronisation
x.join()
y.join()

print(ls)