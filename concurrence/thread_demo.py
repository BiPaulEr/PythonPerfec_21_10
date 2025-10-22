import time
from threading import Thread
import threading

def simple_worker(caractere):
    for i in range(0, 20):
        print(caractere, end="", flush=True)
        time.sleep(1)
    

t1 = Thread(target=simple_worker, args=("*"), name="OUI", daemon=True)
print(f"ident {t1.ident}")
t1.start()
print(f"ident {t1.ident}")
t2 = Thread(target=simple_worker, args=("$"), daemon=True)
t2.start()

print(threading.enumerate())

t1.join()
print("NORMALLY T1 end")