import time

class Stopwatch(object):
    
    def __init__(self):
        """ Create a stopwatch timer
        Parameters:"""
        
        self._stop_time = 0
        self._start_time = 0
        self.elapsed_time = 0
        
    def __repr__(self):
        return 'Stopwatch()'
        
    def start_timer(self):
        """Starts the timer."""
        print("timer started")
        self._start_time = time.time() - self.elapsed_time
        return 
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        print("timer stopped")
        self._stop_time =  time.time()
        
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
        print sec
        minutes, sec = divmod(round(clock_time,2), 60)
        print sec
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
        self.elapsed_time = (time.time() - self._start_time)
        return self.elapsed_time
        
    def reset(self):
        """ Resets the start time to 0. """
        print("timer reset")
        self._start_time = 0
        self._stop_time = 0
        self.elapsed_time = 0
        return 
        

        
        
mytimer = Stopwatch()
 
