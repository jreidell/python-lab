import threading
import time

# Define a function that performs a task
def perform_task(name, duration):
    print(f"Thread {name}: starting")
    time.sleep(duration)  # Simulates a task taking time
    print(f"Thread {name}: finished")

# Create a list to hold our threads
threads = []

# Define number of threads and durations for each task
num_threads = 5
durations = [2, 4, 1, 3, 5]  # each task takes a different amount of time

# Create and start each thread
for i in range(num_threads):
    thread = threading.Thread(target=perform_task, args=(f"Task-{i+1}", durations[i]))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All tasks completed.")
