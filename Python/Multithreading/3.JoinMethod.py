import threading

class MyThread(threading.Thread):
    def run(self):
        # Your thread's code goes here
        print("Thread is running.")


my_thread = MyThread()
my_thread.start()

try:
    my_thread.join()
except KeyboardInterrupt:
    # Handle the KeyboardInterrupt, if necessary
    pass

print("Thread has completed.")