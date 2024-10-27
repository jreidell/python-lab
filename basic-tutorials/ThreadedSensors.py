import threading
import time
import random

# Create a stop event for signaling threads to stop
stop_event = threading.Event()

# Function to monitor distance sensor with a stop check
def monitor_distance_sensor():
    while not stop_event.is_set():  # Continue until the stop event is set
        distance = random.uniform(0.5, 5.0)  # Simulated distance data
        print(f"Distance Sensor: {distance:.2f} meters")
        
        # Use a shorter sleep and check stop_event more frequently
        for _ in range(20):  # Check every 0.1 second for a total 2 seconds
            if stop_event.is_set():
                break
            time.sleep(0.1)

# Function to monitor light sensor with a stop check
def monitor_light_sensor():
    while not stop_event.is_set():  # Continue until the stop event is set
        light_level = random.uniform(0, 1000)  # Simulated light intensity
        print(f"Light Sensor: {light_level:.1f} lumens")
        
        # Use a shorter sleep and check stop_event more frequently
        for _ in range(10):  # Check every 0.1 second for a total 1 second
            if stop_event.is_set():
                break
            time.sleep(0.1)

# Create threads
distance_thread = threading.Thread(target=monitor_distance_sensor)
light_thread = threading.Thread(target=monitor_light_sensor)

# Start threads
distance_thread.start()
light_thread.start()

try:
    # Keep the main program running to allow threads to continue working
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("CTRL+C pressed. Stopping threads...")
    stop_event.set()  # Signal threads to stop

    # Wait for all threads to finish
    distance_thread.join()
    light_thread.join()

    print("All threads stopped. Exiting program.")
