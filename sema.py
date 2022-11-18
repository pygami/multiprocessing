import multiprocessing
import time

def worker_task(task_number, semaphore):
    with semaphore:
        print(f"Task {task_number} started")
        time.sleep(1)
        print(f"Task {task_number} completed")

semaphore = multiprocessing.Semaphore(2)
tasks = [multiprocessing.Process(target=worker_task, args=(i, semaphore)) for i in range(5)]
for task in tasks:
    task.start()
for task in tasks:
    task.join()
