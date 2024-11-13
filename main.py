import time
import random
import keyboard

# Constants
SECONDS_IN_MINUTE = 60
TIME_FORMAT = "{:02d}:{:02d}"

# Variables
TEST_TIMER = 5  # Duration for the test timer in seconds
SHORT_BREAK = 10  # Duration for a short break in seconds
LONG_BREAK = 20  # Duration for a long break in seconds
RANDOM_LONG_BREAK = random.randint(30, 60)  # Random duration for a long break between 30 and 60 seconds
WORK_TIME = 20  # Duration for work time in minutes
WORK_SESSIONS = 4  # Number of work sessions

def start_timer(duration):
    if duration <= 0:
        print("Duration must be a positive integer.")
        return
    
    print("Starting timer...")
    
    for seconds in range(duration * SECONDS_IN_MINUTE, -1, -1):
        minutes = seconds // SECONDS_IN_MINUTE
        remaining_seconds = seconds % 60
        formatted_time = TIME_FORMAT.format(minutes, remaining_seconds)
        print(formatted_time, end='\r')
        time.sleep(1)
    
    print("\nTime's up!")

# Start the timer with test duration
start_timer(TEST_TIMER)