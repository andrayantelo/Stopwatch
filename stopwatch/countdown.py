import stopwatch as st
import time

"""
def countdown(n):
    while n > 0:
        print n
        time.sleep(1)
        n -= 1
    print "Countdown's up!"
        
with st.mytimer:
    countdown(5)
print(st.mytimer.elapsed())
"""

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
        
        
    def countdown(self, start_time):
        """Counts down starting at time.
        Parameters: 
            start_time: int, the time to be counted down from"""
        pass
        
