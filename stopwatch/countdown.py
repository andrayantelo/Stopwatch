import stopwatch as sw
import time
import utilityfunctions as uf
from timeit import default_timer as real_time


class Countdown(object):
    
    
    #11/16/2016 ADDED NAME ATTRIBUTE, THIS WILL BREAK OTHER MODULES THAT USE COUNTDOWN EXCEPT THE POMODORO STUFF
    #CAN REMOVE AFTER SELECTION PROCESS IN POMODORO WORKS
    def __init__(self, timer_func, name):
        """Creates a countdown timer.
        countdown_time: tuple (hh, mm, ss, ms)"""
        
        self.name = name
        self.timer = sw.Stopwatch(timer_func)
        #Convert time into seconds because countdown class works with seconds
        self._countdowntime = 0
    
    def stop_countdown(self):
        """Stops the countdown timer."""
        self.timer.stop_timer()
        
    def start_countdown(self):
        """Starts the countdown timer."""
        self.timer.start_timer()
        
    def time_remaining(self):
        """returns the time left in the countdown"""
        
        return self.countdowntime - self.timer.elapsed()
        
    def reset_countdown(self):
        """Resets the countdown timer."""
        #self.countdown_time = 0
        self.timer.reset()
        
    @property
    def countdowntime(self):
        return self._countdowntime
        
    @countdowntime.setter
    def countdowntime(self, countdown_time):
        """Changes the value of self.countdown_time
        Parameters:
            countdown_time: tuple (hh, mm, ss, ms) """
        if type(countdown_time) != tuple:
            raise TypeError('input must be a tuple (hh, mm. ss, ms)')
            
        self._countdowntime = uf.tuple_to_seconds(countdown_time)
        
        
    def __enter__(self):
        self.start_countdown()
        return self
        
    def __exit__(self, *args):
        self.stop_countdown()
        
if __name__ == '__main__':        
    my_countdown = Countdown(real_time)
    #with t:
    #    while t.time_remaining() > 0:
    #        time.sleep(1)
    #        print t.time_remaining()
    #print "time's up"

 
 
        
