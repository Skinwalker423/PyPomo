import time

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Timer:
    def __init__(self, break_time):
        self.counter = break_time

    def start(self):
        print("starting timer")
        time.sleep(1)
        self.counter -= 1
