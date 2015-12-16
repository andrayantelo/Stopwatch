import stopwatch as st
import time

def countdown(duration):
        """Counts down starting at time.
        Parameters: 
            duration: int (in seconds), the time to be counted down from"""
        start_time = time.time()
        elapsed = 0
        while elapsed < duration:
            print duration - elapsed
            time.sleep(1)
            elapsed = time.time() - start_time
        print "time's up!"

class Countdown(object):
    
    def __init__(self, countdown_time):
        """Creates a countdown timer.
        countdown_time: number of seconds"""
        
        self.timer = st.Stopwatch(st.real_time)
        self.countdown_time = countdown_time
        self.time_left = self.countdown_time
        
        
    def start_countdown(self):
        """Starts the countdown timer."""
        self.timer.start_timer()
        
    def stop_countdown(self):
        """Stops the countdown timer."""
        self.timer.stop_timer()
        
    def time_remaining(self):
        """returns the time left in the countdown"""
        
        self.time_left = self.countdown_time - self.timer.elapsed()
        return self.time_left
        
    def reset_countdown(self):
        """Resets the countdown timer."""
        self.timer.reset()
        self.time_left = 0
        
    def input_countdown_time(self, countdown_time):
        """Changes the value of self.countdown_time
        Parameters:
            countdown_time: tuple of length 4, (hh, mm, ss, ms) """
        self.countdown_time = countdown_time
        
    def __enter__(self):
        self.start_countdown()
        return self
        
    def __exit__(self, *args):
        self.stop_countdown()
        
        
t = Countdown(5)
with t:
    while t.time_left > 0:
        time.sleep(1)
        print t.time_remaining()
print "time's up"

 
        
