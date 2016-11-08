import time
from timeit import default_timer as real_time


class Stopwatch(object):
    
    def __init__(self, timer_func):
        """ Create a stopwatch timer
        Parameters: timer_func"""
        
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
        
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        if self._start_time is None:
            raise RuntimeError('Timer has not been started')
        self._stop_time =  self._now()
        self.elapsed_time += self._stop_time - self._start_time
        
        self._start_time = None

        return

    
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

