import multiprocessing
import time

def producer(queue):
    for i in range(5):
        time.sleep(1)
        item = f"Item {i}"
        queue.put(item)
        print(f"Produced: {item}")

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")

queue = multiprocessing.Queue()
producer_process = multiprocessing.Process(target=producer, args=(queue,))
consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
producer_process.start()
consumer_process.start()
producer_process.join()
queue.put(None)  # Signal consumer to stop
consumer_process.join()
