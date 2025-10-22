from threading import Thread, current_thread, local
from random import randint
from time import sleep

class SharedData:
    value = None

def show_value(data):
    try:
        val = data.value
    except AttributeError:
        print(current_thread().name, ' - No value yet')
    else:
        print(current_thread().name, ' - value =', val)

def worker(data):
    show_value(data)
    data.value = randint(1, 100)
    show_value(data)
    sleep(2)
    show_value(data)
print(current_thread().name, ' - Starting')

shared_data = SharedData()
local_data = local()
show_value(local_data)
local_data.value = 45
print("Starting")
for i in range(2):
    t = Thread(name='W' + str(i), target=worker, args=(local_data,))
    t.start()

print(current_thread().name, ' - Done')