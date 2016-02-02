import stopwatch as sw
import time


class Countdown(object):
    
    def __init__(self, countdown_time, timer_func):
        """Creates a countdown timer.
        countdown_time: tuple (hh, mm, ss, ms)"""
        
        self.timer = sw.Stopwatch(timer_func)
        #Convert time into seconds because countdown class works with seconds
        self.countdown_time = self.timer.revert_time(countdown_time)
    
        
    def start_countdown(self):
        """Starts the countdown timer."""
        self.timer.start_timer()
        
    def stop_countdown(self):
        """Stops the countdown timer."""
        self.timer.stop_timer()
        
    def time_remaining(self):
        """returns the time left in the countdown"""
        
        return self.countdown_time - self.timer.elapsed()
        
    def reset_countdown(self):
        """Resets the countdown timer."""
        self.timer.reset()
        
    def input_countdown_time(self, countdown_time):
        """Changes the value of self.countdown_time
        Parameters:
            countdown_time: tuple (hh, mm, ss, ms) """
        if type(countdown_time) != tuple:
            raise TypeError('input must be a tuple (hh, mm. ss. ms)')
        self.countdown_time = self.timer.revert_time(countdown_time)
        
    def __enter__(self):
        self.start_countdown()
        return self
        
    def __exit__(self, *args):
        self.stop_countdown()
        
if __name__ == '__main__':        
    my_countdown = Countdown((0, 0, 5, 0), sw.real_time)
    #with t:
    #    while t.time_remaining() > 0:
    #        time.sleep(1)
    #        print t.time_remaining()
    #print "time's up"

 
 
        
