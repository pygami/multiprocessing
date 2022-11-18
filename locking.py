import multiprocessing

def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

counter = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

processes = [multiprocessing.Process(target=increment, args=(counter, lock)) for _ in range(4)]
for process in processes:
    process.start()
for process in processes:
    process.join()

print("Counter value with Lock:", counter.value)
