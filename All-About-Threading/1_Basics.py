import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print("Done")
    time.sleep(0.85)
    print("now done")


x = threading.Thread(target=func)
print(threading.active_count())
x.start()
time.sleep(1.2)
print("finally")
print(threading.active_count())