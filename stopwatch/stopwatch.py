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
        self._start_time = 0
        self._start_state = False
        self.elapsed_time = 0
        self._now = timer_func
        
    def __repr__(self):
        return 'Stopwatch()'
        
    def start_timer(self):
        """Starts the timer."""
        if self._start_state:
            raise RuntimeError('Timer already started')
            
        print("timer started")
        self._start_time = self._now() 
        print "this is the start time {:.6f}".format(self._start_time)
    
        self._start_state = True
        print "this is the elapsed time {:.4f}".format(self.elapsed_time)
        return 
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        if not self._start_state:
            raise RuntimeError('Timer has not been started')
        print("timer stopped")
        self._stop_time =  self._now()
        print "this is the stop time {:.6f}".format(self._stop_time)
        #self.elapsed_time = (self._stop_time - self._start_time)
        self.elapsed_time += self._stop_time - self._start_time
        self._start_state = False
        print "this is the elapsed time {:.4f}".format(self.elapsed_time)
        return

    def convert_time(self, clock_time):
        """ Returns a tuple containing the hours, minutes, seconds and
        milliseconds of a time given in seconds.
        
        Parameters:
        clock_time: int
            the time, in seconds, to be converted.
        """
        
        clock_time = clock_time
        milliseconds = clock_time * 1000 
        sec, milliseconds = divmod(round(milliseconds,2), 1000)
        #print sec
        minutes, sec = divmod(round(clock_time,2), 60)
        #print sec
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
        #if it's not running
        #if not self._start_state:
            
        #    self.elapsed_time = self._stop_time - self._start_time
        #    return self.elapsed_time
            
         #if it's running
        if self._start_state:
            return (self._now() - self._start_time) + self.elapsed_time
        #self.start_timer()
        #self.elapsed_time += self.increment
        return self.elapsed_time
        
    def reset(self):
        """ Resets the start time to 0. """
        #print("timer reset")
        self._start_time = 0
        self._stop_time = 0
        self.elapsed_time = 0
        self._start_state = False
        return 
        

mytimer = Stopwatch(fake_time)
 
