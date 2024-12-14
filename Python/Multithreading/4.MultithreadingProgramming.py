import threading
import time

# Thread function 1
def thread_function_1():
    for i in range(5):
        time.sleep(0.01)  # Simulate some time-consuming task
        print("Thread 1: {}".format(i))

# Thread function 2
def thread_function_2():
    for i in range(5):
        time.sleep(0.01)  # Simulate some time-consuming task
        print("Thread 2: {}".format(i))

# Create thread instances
thread_1 = threading.Thread(target=thread_function_1)
thread_2 = threading.Thread(target=thread_function_2)

# Start the threads
thread_2.start()
thread_1.start()

# Wait for both threads to finish
thread_2.join()
thread_1.join()

# Main thread continues here
print("Main thread: Done!")