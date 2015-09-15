import time

class Stopwatch(object):
    
    def __init__(self):
        """ Create a stopwatch timer
        Parameters:"""
        
        self.pause_state = False
        self.time_of_pause = 0
        self.stop_time = 0
        self.pause_duration = 0
        self.elapsed_time = 0
        
    def __repr__(self):
        return 'Stopwatch()'
        
    def _start_timer(self):
        """Starts the timer."""
        
        self.start_time = time.time()
        return self.start_time
    
    def _stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        self.stop_time = time.time()
        return self.stop_time

    def convert_time(self, clock_time):
        """ Returns a tuple containing the minutes and seconds of a time given 
        in seconds.
        
        Parameters:
        clock_time: int
            the time, in seconds, to be converted.
        """
        
        
        clock_time = int(clock_time)
        #milliseconds = clock_time - int(clock_time)  #does not work
        #print milliseconds
        minutes, sec = divmod(clock_time, 60)
        output = (minutes, sec)
        return output
        
    def format_time(self, clock_tuple):
        """ Returns a string of the time in a 'minutes:seconds' format.
        
        Parameters:
        clock_tuple: int
            tuple containing (minutes, seconds).
        """
        formatted_time = "%02d:%02d" %(clock_tuple[0], clock_tuple[1])
        
    def elapsed(self):
        """ Returns the formatted time that has elapsed.
        """
        print("pause duration")
        print self.pause_duration
        self.elapsed_time = time.time() - self.pause_duration
        return self.elapsed_time - self.start_time
        
    def reset(self):
        """ Resets the start time to 0. """
        self.start_time = time.time()
        return self.start_time
        
    def pause(self):
        """ Pauses the stopwatch."""
        
        if not self.pause_state:
            self.time_of_pause = time.time()
            print("time of pause")
            print(self.time_of_pause)
            self.pause_state = True
            print(self.pause_state)
        elif self.pause_state:
            self.pause_duration = time.time() - self.time_of_pause
            self.pause_state = False
            print self.format_time(self.pause_duration)
            return self.pause_duration
            
        

        
        
mytimer = Stopwatch()
 
