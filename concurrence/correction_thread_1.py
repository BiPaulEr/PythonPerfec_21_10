import time
from threading import Thread, Lock
import threading

lock = Lock()

def ecrire():
    with lock, open("compte.txt", "a") as f:
        for i in range(100, 999):
            f.write(str(i).zfill(6))
            f.write(" ")
            f.flush()
    
threads = []
for i in range(0, 100):
    threads.append(Thread(target=ecrire, name="Thread-"+str(i), daemon=True))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("les threads sont terminés")
