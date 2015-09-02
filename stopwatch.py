import time
import subprocess
import sys
import Tkinter as tk
import pygame
from functools import partial
import string
import re
import tkFont

class stopwatch(object):
    
    def __init__(self):
        """ Create a stopwatch timer
        Parameters:"""
        
        
        
    def start_timer(self):
        """Starts the timer."""
        self.start_time = time.time()
        return
    
    def stop_timer(self):
        """ Stops the timer."""
        return

    def format_time(self, clock_time):
        """ Convert time in seconds to a minute:second:millisecond format.
        
        Parameters:
        clock_time: int
            the time to be converted in seconds
        """
        
