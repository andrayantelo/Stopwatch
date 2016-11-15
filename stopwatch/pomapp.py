#pomodoro gui

import countdown as cd
import stopwatch as sw
import pomodoro as pom
import time
import Tkinter as tk
from functools import partial
import utilityfunctions as uf


#I don't want the countdowns to be able to run at the same time

class Pomapp(object):
    
    def __init__(self, master):
        self.master = master
        
        self.pomodoro = pom.Pomodoro()
        
        #making separate frames for the countdowns
        self.break_frame = tk.Frame(self.master).grid(row=0)
        
        self.work_frame = tk.Frame(self.master).grid(row=0)
        
        #giving the gui a title
        self.master.title("Pomodoro")
        
        #making buttons to select the countdown you want to set/use
        self.break_button = tk.Button(self.break_frame, text="Break Time", width = 10, command = lambda: self.select_countdown(self.break_button, self.work_button))
        self.break_button.grid(row=0, column=1)
        
        self.work_button = tk.Button(self.work_frame, text="Work Time", width = 10, command = lambda: self.select_countdown(self.work_button, self.break_button))
        self.work_button.grid(row=0, column=4)
        
        #Making the labels for the break countdown, the labels are where the numbers will be printed
        self.break_label_text = tk.StringVar()
        break_text = uf.seconds_to_string(self.pomodoro.break_countdown.countdowntime)
        self.break_label_text.set(break_text[0])
        #the small text is where the milliseconds are printed
        self.small_break_label_text = tk.StringVar()
        self.small_break_label_text.set(break_text[1])
        
        
        self.break_label = tk.Label(self.break_frame, textvariable=self.break_label_text, width = 10, font=("Arial",16))
        self.break_label.grid(row=1, column=1)
        
        self.small_break_label = tk.Label(self.break_frame, textvariable=self.small_break_label_text, width=5)
        self.small_break_label.grid(row=1, column=2, sticky="w")
        
        #Making the labels for the work countdown
        self.work_label_text = tk.StringVar()
        work_text = uf.seconds_to_string(self.pomodoro.work_countdown.countdowntime)
        self.work_label_text.set(work_text[0])
        
        self.small_work_label_text = tk.StringVar()
        self.small_work_label_text.set(work_text[1])
        
        self.work_label = tk.Label(self.work_frame, textvariable=self.work_label_text, width=10, font=("Arial",16))
        self.work_label.grid(row=1, column=4)
        
        self.small_work_label = tk.Label(self.work_frame, textvariable=self.small_work_label_text, width=5)
        self.small_work_label.grid(row=1, column=5, sticky="w")
        
        #define a dictionary containing labels to associate with their countdowns
        self.countdown_labels = {self.pomodoro.work_countdown : (self.work_label_text, self.small_work_label_text),
                               self.pomodoro.break_countdown : (self.break_label_text, self.small_break_label_text)
                               }
                               
        #define a dictionary containing the countdowns associated with their buttons
        self.countdown_buttons = {self.work_button : self.pomodoro.work_countdown,
                                  self.break_button : self.pomodoro.break_countdown}
        
        #the start/reset/quit buttons get a separate frame
        self.button_frame = tk.Frame(self.master).grid(row=3)
        
        self.start_button = tk.Button(self.break_frame, text="START", fg="green", width=5, command=self.start)
        self.start_button.grid(row=2, column=0)
        self.reset_button = tk.Button(self.break_frame, text="RESET", fg="orange", width=5, command=self.reset)
        self.reset_button.grid(row=2, column=1)
       # self.quit_button = tk.Button(self.break_frame, text="QUIT", fg="red", width=5)
       #self.quit_button.grid(row=2, column=3)
        
        #separate frame for the keypad
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
            button_command = partial(self.callback, label)
            number_button[n] = tk.Button(self.keypad_frame, text=label, width=5, command=button_command)
            number_button[n].grid(row=row, column=column)
            n += 1
            column += 1
            if column > 2:
                column = 0
                row += 1
            if n == 9:
                column = 1
             
        #the actual_output is just the active time's countdown time 
        self.actual_output = ['0','0','0','0','0','0']
        #the temporary_output becomes the actual_output once the pomodoro app is started
        self.temporary_output = ['0','0','0','0','0','0']
        self.callback_counter = 0
        self.reset_counter = 0
                
    def select_countdown(self, selected_button, unselected_button):
        """selects the countdown to start with, either break or work 
        countdown"""
        
        if selected_button.cget("relief") == "raised":
            selected_button.config(relief="sunken")
            unselected_button.config(relief="raised")
        else:
            selected_button.config(relief="raised")
            unselected_button.config(relief="sunken")
        
        #make the selected countdown the active countdown
        self.pomodoro.active_countdown = self.countdown_buttons[selected_button]
        
                
    def play_alert(self):
        """plays the time's up alert sound"""
        pass
        
    def toggle_red(self):
        """makes the background of the appropriate label flash red"""
        pass
        
    def callback(self, label):
        """defines what happens when you press on one of the keys on the
        keypad"""
        
        try:
            if self.pomodoro.active_countdown.timer.running:
                raise RuntimeError("Timer is currently running")
            elif self.callback_counter == 6:
                self.temporary_output = ['0','0','0','0','0','0']
                self.callback_counter = 0
                return
            self.reset_counter = 0
        # take off first element in large_output, and add label (keypad number pressed) to the end
            self.temporary_output.pop(0)
            self.temporary_output.append(label)
            
            self.callback_counter += 1
        except RuntimeError:
            print "The timer is currently running."
        finally:
            self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.list_to_clockface(self.temporary_output))

            
        
    def print_to_countdown(self):
        """prints how much time is left in the countdown"""
        
        """write out what's supposed to happen
        if the countdown is running, it needs to continuously update
        the labels so that they display the correct time that is left 
        in the countdown"""
        
        if self.pomodoro.active_countdown.timer.running:
            output = uf.sec_to_clockface(self.pomodoro.time_remaining())
            self.countdown_labels[self.pomodoro.active_countdown][0].set(output[0])
            self.countdown_labels[self.pomodoro.active_countdown][1].set(output[1])
            
            if self.pomodoro.active_countdown.time_remaining() < 0:
                self.stop()
                #the following two lines are done so that you don't end up with negative
                #numbers on the number display on the gui
                
                self.start_button.config(text = "START")
                self.countdown_labels[self.pomodoro.active_countdown][0].set("00:00:00")
                self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
                
            
            self.master.after(50, self.print_to_countdown)
        
    def start(self):
        """starts the countdown (the countdown that is selected)"""
        #Set the active countdown's time to the input the user gave with the keypad
        self.actual_output = self.temporary_output
        self.pomodoro.active_countdown.countdowntime = uf.list_to_tuple(self.actual_output)
        self.reset_counter = 0
       
        #won't run if there isn't a countdown time
        if self.pomodoro.active_countdown.time_remaining() <= 0:
            raise RuntimeError('Time remaining is zero, input a countdown time')
        
        
        if self.pomodoro.active_countdown.timer.running:
            self.stop()
            self.print_to_countdown()
            self.start_button.config(text = "START")
            
            print self.pomodoro.active_countdown.timer.running
        else:  
            self.pomodoro.active_countdown.start_countdown()
            self.print_to_countdown()
            self.start_button.config(text = "PAUSE")  
            
            print self.pomodoro.active_countdown.timer.running
        
    def stop(self):
        """stops the selected countdown"""
        self.pomodoro.active_countdown.stop_countdown()
        print self.pomodoro.active_countdown.timer.running
        
    def reset(self):
        """resets the selected countdown"""
        
        if self.reset_counter == 0:
            self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.list_to_clockface(self.actual_output))
            self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
            
        elif self.reset_counter >= 1:
            self.reset_counter = 0
            self.pomodoro.reset_pomodoro()
            self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.sec_to_clockface(self.pomodoro.active_countdown.countdowntime)[0])
            self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
        self.reset_counter += 1
        print self.reset_counter
        
        
       
        

def main():
    """run main."""
    #creating the root window of our application with the Tk class
    root = tk.Tk()
    a = Pomapp(root)
    root.mainloop()
        
if __name__ == '__main__':
    main()
        
