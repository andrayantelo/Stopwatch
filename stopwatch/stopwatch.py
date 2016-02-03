import time
from timeit import default_timer as real_time

def make_fake_time_function(test_numbers):
    nums = iter(test_numbers)
    def fake_time():
        return nums.next()
    return fake_time
    
fake_time = make_fake_time_function(range(10000))

class Stopwatch(object):
    
    def __init__(self, timer_func):
        """ Create a stopwatch timer
        Parameters:"""
        
        self._stop_time = 0
        self._start_time = None
        self.elapsed_time = 0
        self._now = timer_func
        
    def start_timer(self):
        """Starts the timer."""
        if self._start_time is not None:
            raise RuntimeError('Timer already started')
            
        self._start_time = self._now() 
        self._start_state = True
        
        return 
        
    def _toggle_start_time(self):
        """Toggles the start_time from None to Not None or vice versa."""
        if self._start_time is None:
            self._start_time = 0
        
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        if self._start_time is None:
            raise RuntimeError('Timer has not been started')
        self._stop_time =  self._now()
        self.elapsed_time += self._stop_time - self._start_time
        
        self._start_time = None

        return

    def convert_time(self, clock_time):
        """ Returns a tuple containing the hours, minutes, seconds 
        of a time given in seconds.
        
        Parameters:
        clock_time: int
            the time, in seconds, to be converted.
        """
        
        if type(clock_time) == tuple and len(clock_time) == 3:
            return clock_time
        
        milliseconds = clock_time * 1000
        sec, milliseconds = divmod(round(milliseconds,2), 1000)
        minutes, sec = divmod(round(clock_time,2), 60)
        hours, minutes = divmod(round(minutes,2), 60)
        output = (int(hours), int(minutes), int(sec), milliseconds)
        
        return output
        
    def revert_time(self, time_tuple):
        """ Takes a tuple and converts it to time in seconds.
        
        Parameters:
        time_tuple: tupe
            tuple containing (hours, minutes, sec, milliseconds).
        {hh, mm, ss) -> sec
        """
        if type(time_tuple) != tuple:
            raise TypeError('Must input a tuple containing hh, mm, ss, ms')
            
        hour = time_tuple[0] * 3600
        minutes = time_tuple[1] * 60
        sec = time_tuple[2] 
        milliseconds = time_tuple[3] * 0.001
        
        return hour + minutes + sec + milliseconds
        
    def format_time(self, clock_tuple):
        """ Returns tuple of the time in a (('hour:minutes:seconds'), ms) format.
        
        Parameters:
        clock_tuple: int
            tuple containing (hours, minutes, sec, ms).
        """
        formatted_time = "%02d:%02d:%02d" %(clock_tuple[0], clock_tuple[1], clock_tuple[2])
        formatted_milliseconds = "%03d" %clock_tuple[3]
        
        return (formatted_time, formatted_milliseconds)
        
    def elapsed(self):
        """ Returns the time that has elapsed between starting the timer
            and stopping it.
        """
        
        #if it's running
        if self._start_time is not None:
            return (self._now() - self._start_time) + self.elapsed_time
        
        return self.elapsed_time
        
    def reset(self):
        """ Resets the start time to 0. """
        
        self._start_time = 0
        self._stop_time = 0
        self.elapsed_time = 0
        self._start_time = None
        
        return 
        
    @property
    def running(self):
        return self._start_time is not None
        
    def __enter__(self):
        self.start_timer()
        return self
        
    def __exit__(self, *args):
        self.stop_timer()
 

if __name__ == '__main__':
    mytimer = Stopwatch(real_time)

