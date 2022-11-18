import multiprocessing

def square_list(numbers, result, index, lock):
    for i, num in enumerate(numbers):
        with lock:
            print(f"Process {index}: Squaring {num}")
            result[i] = num * num

numbers = [1, 2, 3, 4, 5]
result = multiprocessing.Array('i', len(numbers))
lock = multiprocessing.Lock()

processes = [multiprocessing.Process(target=square_list, args=(numbers, result, i, lock)) for i in range(2)]
for process in processes:
    process.start()
for process in processes:
    process.join()

print("Squared list:", list(result))


def increment(value):
    value.value += 1

value = multiprocessing.Value('i', 0)
processes = [multiprocessing.Process(target=increment, args=(value,)) for _ in range(4)]
for process in processes:
    process.start()
for process in processes:
    process.join()

print("Final value with Value:", value.value)