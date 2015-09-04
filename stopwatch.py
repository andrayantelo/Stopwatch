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
        
    def start_timer(self):
        """Starts the timer."""
        
        self.start_time = time.time()
        return
    
    def stop_timer(self):
        """ Stops the timer. Returns time elapsed."""
        
        self.stop_time = time.time()
        
        return self.stop_time - self.start_time

    def format_time(self, clock_time):
        """ Convert time in seconds to a minute:second format.
        
        Parameters:
        clock_time: int
            the time to be converted in seconds
        """
        minutes, sec = divmod(clock_time, 60)
        output = "%02d:%02d" % (minutes, sec)
        return output
        
mytimer = Stopwatch()
 
