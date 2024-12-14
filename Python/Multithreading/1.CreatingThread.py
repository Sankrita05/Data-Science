import threading
class MyThread(threading.Thread):
    def run(self):
        # Code to be executed in the thread
        print("Thread is running")

# Create an instance of the custom thread class
my_thread = MyThread()
my_thread.start()

my_thread.join()
print("Thread has finished.")
