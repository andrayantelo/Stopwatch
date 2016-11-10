#pomodoro gui

import countdown as cd
import stopwatch as sw
import time
import Tkinter as tk
from functools import partial
import utilityfunctions as uf


class Pomapp(object):
    
    def __init__(self, master):
        self.master = master
        self.mycountdown = cd.Countdown(sw.real_time)
        self.mytimer = sw.Stopwatch(sw.real_time)
        
        self.break_frame = tk.Frame(self.master).grid(row=0)
        
        self.work_frame = tk.Frame(self.master).grid(row=0)
        
        self.master.title("Pomodoro")
        
        self.break_label = tk.Label(self.break_frame, text="break time", width = 10).grid(row=0, column=0)
        self.work_label = tk.Label(self.work_frame, text="work time", width = 10).grid(row=0, column=4)
        
        self.button_frame = tk.Frame(self.master).grid(row=1)
        
        self.start_button = tk.Button(self.break_frame, text="START", fg="green", width=5).grid(row=1, column=0)
        self.reset_button = tk.Button(self.break_frame, text="RESET", fg="orange", width=5).grid(row=1, column=1)
        self.quit_button = tk.Button(self.break_frame, text="QUIT", fg="red", width=5).grid(row=1, column=3)
        

def main():
    """run main."""
    #creating the root window of our application with the Tk class
    root = tk.Tk()
    a = Pomapp(root)
    root.mainloop()
        
if __name__ == '__main__':
    main()
        
