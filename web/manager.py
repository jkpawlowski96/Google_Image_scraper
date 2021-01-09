import queue
import time
class Manager:
    port_start = 6731
    def __init__(self):
        self.tasks = Queue()
        self.workers = []
        self.num_workers = 0
        self.max_workers = 1

    def init(self):
        for i in range self.max_workers:
            worker = Worker(i, self.port_start + i)
            self.workers.append(worker)

    def add_task(task:Task):
        self.tasks.push(task)

    @static_method
    def loop(tasks, workers):
        while(True):
            
            time.sleep(1)
            


class Worker:
    def __init__(self, id, port)
        self.id = id
        self.port = port
        # run worker cmd in new process or in backend

class Task:
    def __init__(self):
        pass