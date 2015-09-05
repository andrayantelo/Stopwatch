import time
import subprocess
import sys
import Tkinter as tk
import pygame
from functools import partial
import string
import re
import tkFont

class Stopwatch(object):
    
    def __init__(self):
        """ Create a stopwatch timer
        Parameters:"""
        
        pass
        
    def __repr__(self):
        return 'stopwatch(%s,%s)' % ()
        
    def _start_timer(self, start_time):
        """Starts the timer."""
        
        self.start_time = start_time
        return
    
    def _stop_timer(self):
        """ Stops the timer. Returns time elapsed."""
        
        self.stop_time = time.time()
        
        return self.stop_time - self.start_time

    def format_time(self, clock_time):
        """ Convert time in seconds to a minute:second:millisecond format.
        
        Parameters:
        clock_time: int
            the time to be converted in seconds
        """
        
        
        clock_time = int(clock_time)
        #milliseconds = clock_time - int(clock_time)  #does not work
        #print milliseconds
        minutes, sec = divmod(clock_time, 60)
        output = "%02d:%02" % (minutes, sec)
        return output
        
    def elapsed(self):
        """ Returns the formatted time that has elapsed.
        """
        return time.time() - self.start_time
        
    def reset(self):
        """ Resets the start time to 0. """
        self.start_time = time.time()
        return self.start_time
        
    def pause(self):
        """ Pauses the stopwatch."""
        
        time_of_pause = self.elapsed()
        mytimer._stop_timer()
        return time_of_pause
        

        
        
mytimer = Stopwatch()
 
