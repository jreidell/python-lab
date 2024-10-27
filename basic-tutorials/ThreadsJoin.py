import threading
import time

def task(name, duration):
    print(f"{name} starting")
    time.sleep(duration)
    print(f"{name} finished")

# Creating two threads
thread1 = threading.Thread(target=task, args=("Thread-1", 3))
thread2 = threading.Thread(target=task, args=("Thread-2", 1))

# Starting the threads
thread1.start()
thread2.start()

# Waiting for thread1 to complete before moving on
thread1.join()
print("Thread-1 has completed")

# Waiting for thread2 to complete before moving on
thread2.join()
print("Thread-2 has completed")

print("Both threads have finished, resuming main program")
