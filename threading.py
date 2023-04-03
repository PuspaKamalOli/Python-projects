import threading

def worker(num):
    """Thread worker function"""
    print(f"Worker {num} starting...")
    print("Worker {num} exiting...")

# Create two threads
thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker, args=(2,))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
