import threading
import queue

# Create a queue and populate it with numbers 1 to 100
task_queue = queue.Queue()
for i in range(1, 101):
    task_queue.put(i)

# Create a lock to synchronize access to the queue
queue_lock = threading.Lock()

# Function to process items from the queue
def process_queue():
    while not task_queue.empty():
        # Ensure only one thread accesses the queue at a time
        with queue_lock: 
            # Double-check if the queue is not empty
            if not task_queue.empty():
                item = task_queue.get()
                print(f"Thread {threading.current_thread().name}: {item}")

# Create and start 5 threads
num_threads = 5
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=process_queue, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
