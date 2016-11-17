#pomodoro gui

import countdown as cd
import stopwatch as sw
import pomodoro as pom
import time
import Tkinter as tk
from functools import partial
import utilityfunctions as uf
import pygame as pg


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
        self.countdown_button = {self.work_button : self.pomodoro.work_countdown,
                                  self.break_button : self.pomodoro.break_countdown}
        
        #the start/reset/quit buttons get a separate frame
        self.button_frame = tk.Frame(self.master).grid(row=3)
        
        self.start_button = tk.Button(self.break_frame, text="START", fg="green", width=5, command=self.start)
        self.start_button.grid(row=2, column=0)
        self.reset_button = tk.Button(self.break_frame, text="RESET", fg="orange", width=5, command=self.reset)
        self.reset_button.grid(row=2, column=1)
        self.stop_button = tk.Button(self.break_frame, text="STOP", fg="red", width=5, command=self.stop)
        self.stop_button.grid(row=2, column=3)
        
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
        #dictionary containing the countdowns with their associated display outputs
        self.actual_output = {self.pomodoro.work_countdown: ['0','0','0','0','0','0'],
                              self.pomodoro.break_countdown: ['0','0','0','0','0','0']}
                              
        #this dictionary will ensure that each countdown has it's own callback counter
        self.callback_counter = {self.pomodoro.work_countdown: 0,
                                  self.pomodoro.break_countdown: 0}
        
        #ensure each countdown has it's own reset counter
        self.reset_counter = {self.pomodoro.work_countdown: 0,
                              self.pomodoro.break_countdown: 0}
                
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
        self.pomodoro.active_countdown = self.countdown_button[selected_button]
        print "this is now the current countdown: " + str(self.pomodoro.active_countdown.name)
        
                
    def play_alert(self):
        """plays the time's up alert sound"""
        
        pg.mixer.init()
        time_up = pg.mixer.Sound("backupdings.wav")
        time_up.play()
        
    def toggle_red(self):
        """makes the background of the appropriate label flash red"""
        pass
        
    def callback(self, label):
        """defines what happens when you press on one of the keys on the
        keypad"""
        
        print "this is the self.actual_output of {} at the beginning of callback".format(self.pomodoro.active_countdown.name) \
        + str(self.actual_output[self.pomodoro.active_countdown])
        print "this is the callback counter of {} at beginning of callback ".format(self.pomodoro.active_countdown.name) \
         + str(self.callback_counter[self.pomodoro.active_countdown])
        
        try:
            if self.pomodoro.active_countdown.timer.running:
                raise RuntimeError("Timer is currently running")
                
            if self.callback_counter[self.pomodoro.active_countdown] == 6:
                print "the program is about to make self.actual output equal to 0"
                self.actual_output[self.pomodoro.active_countdown] = ['0','0','0','0','0','0']
                self.callback_counter[self.pomodoro.active_countdown] = 0
                #return
            
            
            self.reset_counter[self.pomodoro.active_countdown] = 0
        # take off first element in large_output, and add label (keypad number pressed) to the end
            self.actual_output[self.pomodoro.active_countdown].pop(0)
            self.actual_output[self.pomodoro.active_countdown].append(label)
            self.callback_counter[self.pomodoro.active_countdown] += 1
            
            
        except RuntimeError:
            print "The timer is currently running."
        finally:
            self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.list_to_clockface(self.actual_output[self.pomodoro.active_countdown]))
            
            print "this is the self.actual output of {} at end of callback".format(self.pomodoro.active_countdown.name) \
            + str(self.actual_output[self.pomodoro.active_countdown])
            print "this is the callback counter of {} at end of callback".format(self.pomodoro.active_countdown.name) \
            + str(self.callback_counter[self.pomodoro.active_countdown])
            
        
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
                
                #self.countdown_labels[self.pomodoro.active_countdown][0].set("00:00:00")
                #self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
                self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.sec_to_clockface(self.pomodoro.active_countdown.countdowntime)[0])
                self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
                
                #the next line is done so that after a countdown is done, if you input a number, it starts from 0 - NOT NEEDED?
                #self.actual_output[self.pomodoro.active_countdown] = ['0','0','0','0','0','0']
                #self.callback_counter[self.pomodoro.active_countdown] = 0
                
                print "this is the self.actual output of {} right before toggling countdowns: ".format(str(self.pomodoro.active_countdown.name)) \
                 + str(self.actual_output[self.pomodoro.active_countdown])
                print "this is the countdowntime of {} right before you toggle countdowns: ".format(str(self.pomodoro.active_countdown.name)) \
                 + str(self.pomodoro.active_countdown.countdowntime)
                
                self.toggle_countdown()
                
            
            self.master.after(50, self.print_to_countdown)
            
            
    def toggle_countdown(self):
        """this will toggle the countdown, and start it."""
        
        print "toggling countdowns"
        
        
        self.pomodoro.toggle_countdown()
        #the next line ensures that the time_remaining is not less than zero, if it's less than zero the countdown won't start
        self.pomodoro.reset_pomodoro()
        
        print "this is now the active_countdown: " + self.pomodoro.active_countdown.name
        print "this is the self.actual output of {} right after toggling countdowns: ".format(str(self.pomodoro.active_countdown.name)) \
            + str(self.actual_output[self.pomodoro.active_countdown])
        print "this is the countdowntime of {} right after you toggle countdowns: ".format(str(self.pomodoro.active_countdown.name)) \
            + str(self.pomodoro.active_countdown.countdowntime)
            
            
        self.start()
        
        
    def start(self):
        """starts the countdown (the countdown that is selected)"""
        #Set the active countdown's time to the input the user gave with the keypad
        print "this is the time remaining at the beginning of the start method: " + str(self.pomodoro.time_remaining())
        self.pomodoro.active_countdown.countdowntime = uf.list_to_tuple(self.actual_output[self.pomodoro.active_countdown])
        print "this is the time remaining after the first line in start method: " + str(self.pomodoro.time_remaining())
        self.reset_counter[self.pomodoro.active_countdown] = 0
       
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
        self.start_button.config(text = "START")
        print self.pomodoro.active_countdown.timer.running
        
    def reset(self):
        """resets the selected countdown"""
        print "this is the reset_counter of {} at the beginning of reset ".format(self.pomodoro.active_countdown.name) \
         + str(self.reset_counter[self.pomodoro.active_countdown])
        print "this is the self.actual_output of {} at the beginning being reset ".format(self.pomodoro.active_countdown.name) \
         + str(self.actual_output[self.pomodoro.active_countdown])
        print "this is the callback counter of {} at beginning of reset: ".format(self.pomodoro.active_countdown.name) \
         + str(self.callback_counter[self.pomodoro.active_countdown])
        
        
        if self.reset_counter[self.pomodoro.active_countdown] >= 1:
            self.reset_counter[self.pomodoro.active_countdown] = 0
            #self.callback_counter[self.pomodoro.active_countdown] = 0   
            self.pomodoro.active_countdown.countdowntime = (0,0,0,0)
            #self.actual_output[self.pomodoro.active_countdown] = ['0','0','0','0','0','0']
            #print "this is the countdowntime right after setting it equal to zero: " + str(self.pomodoro.active_countdown.countdowntime)
            
        
        self.pomodoro.reset_pomodoro()
        
        self.reset_counter[self.pomodoro.active_countdown] += 1
        #self.callback_counter[self.pomodoro.active_countdown] = 0
        
        #have the gui display the countdown's countdowntime obtained from the countdown object
        self.countdown_labels[self.pomodoro.active_countdown][0].set(uf.sec_to_clockface(self.pomodoro.active_countdown.countdowntime)[0])
        self.countdown_labels[self.pomodoro.active_countdown][1].set("000")
        
        #set the actual output using the countdowntime of the countdown object
        self.actual_output[self.pomodoro.active_countdown] = uf.sec_to_list(self.pomodoro.active_countdown.countdowntime)
        
        
        
        print "this is the reset_counter of {} at the end of reset ".format(self.pomodoro.active_countdown.name) \
         + str(self.reset_counter[self.pomodoro.active_countdown])
        print "this is the self.actual_output of {} after being reset ".format(self.pomodoro.active_countdown.name) \
         + str(self.actual_output[self.pomodoro.active_countdown])
             
        print "this is the call_back counter of {} at end of reset: ".format(self.pomodoro.active_countdown.name) \
         + str(self.callback_counter[self.pomodoro.active_countdown])
        
#TODO:
#FIX RESET *
#HAVE THE COUNTDOWN SELECTION PROCESS ACTUALLY WORK *
#WHEN A COUNTDOWN FINISHES, I WANT IT'S COUNTDOWN TIME DISPLAYED WHILE THE OTHER COUNTDOWN IS GOING *
#FIGURE OUT WHAT TO DO WTIH START/PAUSE.. *
#HAVE THE COUNTDOWNS ACTUALLY TOGGLE
#when a timer has stopped, it show's it's countdown time that you input, so you click reset, it appears like nothing happens
    #need to have it reset to 0
#when your timer ends, figure out what you want to happen when the user tries to input a number without resetting first. 
    #in the countdown app, it appears that the countdown has reset
#ADD BELLS AND WHISTLES  
#ADD BETTER COMMENTS
#FIX A FEW FORMATTING ISSUES      
       
        
#THE PROBLEM: COUNTDOWN ENDS, CLICK RESET ONCE, TRY TO START AGAIN AND IT FAILS *
def main():
    """run main."""
    #creating the root window of our application with the Tk class
    root = tk.Tk()
    a = Pomapp(root)
    root.mainloop()
        
if __name__ == '__main__':
    main()
        
