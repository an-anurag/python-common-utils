import imp


import time
import threading


class Scheduler:
    
    def __init__(self, task, frequency):
        
        self.task = task
        self.frequency = frequency
        
    def every(self):
        next_call_time = time.time() + self.frequency
        while True:
            time.sleep(max(0, next_call_time - time.time()))
            try:
                self.task()
            except Exception as err:
                logger.exception(f"Problem while executing repetitive task: {err}")
            # skip tasks if we are behind schedule:
            next_call_time += (time.time() - next_call_time) // self.frequency * self.frequency + self.frequency
            
    def schedule(self):
        threading.Thread(target=lambda: self.every()).start()



def job():
    print(threading.active_count())
    print("anurag")


scheduler = Scheduler(job, 3)
# scheduler.schedule()


d = {1:2, 3:4}

for k, v in d.items(): print(k, v)