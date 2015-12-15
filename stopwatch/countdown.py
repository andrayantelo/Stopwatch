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
    
    def __init__(self):
        """Creates a countdown timer."""
        self.timer = st.Stopwatch(st.real_time)
        
    def __repr__(self):
        return 'Countdown()'
        
    def start_countdown(self):
        """Starts the countdown timer."""
        pass
        
    def stop_countdown(self):
        """Stops the countdown timer."""
        pass
        
    def reset_countdown(self):
        """Resets the countdown timer."""
        pass
        
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
        
        
 
        
