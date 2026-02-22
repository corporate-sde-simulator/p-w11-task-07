"""Performance monitoring helper. Clean file."""
import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0

    def start(self): self.start_time = time.time()
    def stop(self):
        if self.start_time:
            self.elapsed = time.time() - self.start_time
            self.start_time = None
    def get_ms(self): return round(self.elapsed * 1000, 2)
