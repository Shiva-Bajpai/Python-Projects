import time

def stopwatch():
    print("Press ENTER to start the stopwatch. Press Ctrl+C to stop.")
    input()
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {round(elapsed_time, 2)} seconds", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

stopwatch()
