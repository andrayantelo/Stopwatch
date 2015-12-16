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
        """Creates a countdown timer."""
        self.timer = st.Stopwatch(st.real_time)
        self.countdown_time = countdown_time
        self.time_left = 0
        self._start_state = False
        
    def __repr__(self):
        return 'Countdown()'
        
    def start_countdown(self):
        """Starts the countdown timer."""
        self.timer.start_timer()
        self._start_state = True
        
    def stop_countdown(self):
        """Stops the countdown timer."""
        self.timer.stop_timer()
        self._start_state = False
        self.time_left = self.convert_time(self.countdown_time) - self.timer.elapsed()
        
    def time_remaining(self):
        """returns the time left in the countdown"""
        
        #if countdown is still running
        if self._start_state:
            self.time_left =  self.convert_time(self.countdown_time) - self.timer.elapsed()
            return self.time_left
        
        # if countdown is not running
        else:
            return self.time_left
        
    def reset_countdown(self):
        """Resets the countdown timer."""
        self.timer.reset()
        self.time_left = 0
        self._start_state = False
        
    def input_countdown_time(self, countdown_time):
        """Changes the value of self.countdown_time
        Parameters:
            countdown_time: tuple of length 4, (hh, mm, ss, ms) """
        self.countdown_time = countdown_time
        
    def convert_time(self, time):
        """Takes a time given in hh:mm:ss:ms format and returns the number
        of seconds it corresponds to.
        Parameters:
            time: tuple format (hh, mm, ss, ms) 
        """
        if len(time) != 4:
            raise RuntimeError("time tuple is not of length 4")
        hours = time[0]*3600
        minutes = time[1]*60
        sec = time[2]
        millisec = time[3]*.001
        
        total = hours + minutes + sec + millisec
        return total
        
        
t = Countdown((00, 00, 15, 00))
while t.time_left > 0:
    pass
 
        
