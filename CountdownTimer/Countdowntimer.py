import time

def countdown_timer(seconds):
    while seconds:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    secs = int(input("Enter countdown time in seconds: "))
    countdown_timer(secs)