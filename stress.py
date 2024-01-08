import concurrent.futures
import requests
import argparse
import time
import threading

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple multi-threaded website tester")
    parser.add_argument("url", help="The URL to test")
    parser.add_argument("threads", type=int, help="Number of threads to use")
    parser.add_argument("duration", type=int, help="Total number of seconds to test for")
    
    args = parser.parse_args()

    target_url = args.url
    num_threads = args.threads
    duration = args.duration

    success_counter = Counter()
    failure_counter = Counter()
    total_counter = Counter()

    exit_event = threading.Event()

    def make_request(url):
        while not exit_event.is_set():
            try:
                response = requests.get(url)
                # Add any additional processing based on your testing requirements
                success_counter.increment()
                total_counter.increment()
            except Exception as e:
                print(f"Error making request to {url}: {str(e)}")
                failure_counter.increment()

    def track_results():
        start_time = time.time()
        while not exit_event.is_set():
            elapsed_time = time.time() - start_time
            remaining_time = max(0, duration - elapsed_time)
            requests_per_second = total_counter.value / max(elapsed_time, 1)
            print(f"Time Remaining: {int(remaining_time)}s | Requests per Second: {requests_per_second:.2f} | "
                  f"Successes: {success_counter.value}, Failures: {failure_counter.value}", end='\r')
            time.sleep(1)

    # Start a thread to track results
    result_thread = threading.Thread(target=track_results)
    result_thread.start()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(make_request, target_url) for _ in range(num_threads)]

        # Wait for the specified duration
        time.sleep(duration)

        # Set the exit event to signal threads to stop
        exit_event.set()

    # Wait for the result thread to finish
    result_thread.join()

    print("\nTesting completed.")

