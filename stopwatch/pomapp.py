#pomodoro gui

import countdown as cd
import stopwatch as sw
import time
import Tkinter as tk
from functools import partial
import utilityfunctions as uf


class Pomapp(object):
    
    def __init__(self):
        self.mycountdown = cd.Countdown(sw.real_time)
        self.mytimer = cd.Stopwatch(sw.real_time)
        
        
        
