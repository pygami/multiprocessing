import multiprocessing
import time

def countdown(event):
    print("Countdown started")
    time.sleep(3)
    print("Countdown finished")
    event.set()

def celebrate(event):
    print("Waiting for countdown to finish")
    event.wait()
    print("Happy New Year!")

event = multiprocessing.Event()
t1 = multiprocessing.Process(target=countdown, args=(event,))
t2 = multiprocessing.Process(target=celebrate, args=(event,))
t1.start()
t2.start()
t1.join()
t2.join()
