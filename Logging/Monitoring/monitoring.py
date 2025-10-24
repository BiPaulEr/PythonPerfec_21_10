import schedule, psutil
import time

def job():
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU USAGE", {cpu_usage})

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)