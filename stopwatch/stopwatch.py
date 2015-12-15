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
        
    def __repr__(self):
        return 'Stopwatch()'
        
    def start_timer(self):
        """Starts the timer."""
        if self._start_time is not None:
            raise RuntimeError('Timer already started')
            
        self._start_time = self._now() 
        self._start_state = True
        
        return 
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        if self._start_time is None:
            raise RuntimeError('Timer has not been started')
        self._stop_time =  self._now()
        self.elapsed_time += self._stop_time - self._start_time
        
        self._start_time = None

        return

    def convert_time(self, clock_time):
        """ Returns a tuple containing the hours, minutes, seconds and
        milliseconds of a time given in seconds.
        
        Parameters:
        clock_time: int
            the time, in seconds, to be converted.
        """
        
        milliseconds = clock_time * 1000 
        sec, milliseconds = divmod(round(milliseconds,2), 1000)
        minutes, sec = divmod(round(clock_time,2), 60)
        hours, minutes = divmod(round(minutes,2), 60)
        output = (hours, minutes, sec, milliseconds)
        
        return output
        
    def format_time(self, clock_tuple):
        """ Returns tuple of the time in a (('hour:minutes:seconds'), 'milliseconds') format.
        
        Parameters:
        clock_tuple: int
            tuple containing (hours, minutes, sec, milliseconds).
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
        
    def __exit__(self):
        self.stop_timer()
        
        
mytimer = Stopwatch(real_time)
 

def countdown(n):
    while n > 0:
        print n
        time.sleep(1)
        n -= 1
    print "Countdown's up!"
        
with mytimer
    countdown(5)
print(mytimer.elapsed())

