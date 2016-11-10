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
        
        self.break_button = tk.Button(self.break_frame, text="Break Time", width = 10).grid(row=0, column=1)
        self.work_button = tk.Button(self.work_frame, text="Work Time", width = 10).grid(row=0, column=4)
        
        self.break_label = tk.Label(self.break_frame, text="00:00:00", width = 10, font=("Arial",16))
        self.break_label.grid(row=1, column=1)
        self.work_label = tk.Label(self.work_frame, text="00:00:00", width=10, font=("Arial",16))
        self.work_label.grid(row=1, column=4)
        
        self.button_frame = tk.Frame(self.master).grid(row=3)
        
        self.start_button = tk.Button(self.break_frame, text="START", fg="green", width=5)
        self.start_button.grid(row=2, column=0)
        self.reset_button = tk.Button(self.break_frame, text="RESET", fg="orange", width=5)
        self.reset_button.grid(row=2, column=1)
        self.quit_button = tk.Button(self.break_frame, text="QUIT", fg="red", width=5)
        self.quit_button.grid(row=2, column=3)
        
        self.keypad_frame = tk.Frame(self.master).grid(row=2)
        
        #list of labels for the keypad buttons
        self.keypad_button_list = ['1','2','3',
                                   '4','5','6',
                                   '7','8','9',
                                   '0']
        
        row=4
        column=0
        n=0
        #makes the list [0,1,2,3,4,5,6,7,8,9]
        #list() is there for python3 support. in python 2.7 it is redundant
        #in python3 range returns a range object
        number_button = list(range(len(self.keypad_button_list)))
        
        for label in self.keypad_button_list:
            #this will be where you assign the command for each button
            #button_command = partial(self.callback, label)
            number_button[n] = tk.Button(self.keypad_frame, text=label, width=5)
            number_button[n].grid(row=row, column=column)
            n += 1
            column += 1
            if column > 2:
                column = 0
                row += 1
            if n == 9:
                column = 1
                
    def select_countdown(self):
        """selects the countdown to start with, either break or work 
        countdown"""
        pass
                
                
    def play_alert(self):
        """plays the time's up alert sound"""
        pass
        
    def toggle_red(self):
        """makes the background of the appropriate label flash red"""
        pass
        
    def callback(self, label):
        """defines what happens when you press on one of the keys on the
        keypad"""
        pass
        
    def print_to_countdown(self):
        """prints how much time is left in the countdown"""
        pass
        
    def start(self):
        """starts the countdown (the countdown that is selected)"""
        pass
        
    def stop(self):
        """stops the selected countdown"""
        pass
        
    def reset(self):
        """resets the selected countdown"""
        pass
        
        
       
        

def main():
    """run main."""
    #creating the root window of our application with the Tk class
    root = tk.Tk()
    a = Pomapp(root)
    root.mainloop()
        
if __name__ == '__main__':
    main()
        
