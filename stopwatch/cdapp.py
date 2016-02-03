import countdown as cd
import stopwatch as sw
import time
import Tkinter as tk
from functools import partial

def hide_me(event):
    event.widget.pack_forget()

def convert_time_input(time):
    """Takes a time given in hh:mm:ss format and returns a list
    [h,h,m,m,s,s].
    Parameters:
    time: string format 'hh:mm:ss' 
    """
    new_time = ''
    for letter in time:
        if letter != ':':
            new_time += letter
    new_time = list(new_time)
    if len(new_time) != 6:
        raise RuntimeError("Time list is not of length 6")

    return new_time
    
def revert_time_input(time):
    """Takes a time list in [h, h, m, m, s, s] format and returns a tuple
    (hh, mm, ss).
    Parameters:
    time: list format [h,h,m,m,s,s]
    [h,h,m,m,s,s] -> (hh,mm,ss)
    """
    new_time = ''
    for element in time:
        new_time += str(element)
    
    n = 2
    new_time = [new_time[i:i+n] for i in range(0, len(new_time), n)]
    new_time = tuple([int(i) for i in new_time])
    new_tuple = (new_time[0], new_time[1], new_time[2], 00)
        
    return new_tuple

        
class Cdapp(object):
    #Cdapp class works with tuples for the time
    def __init__(self):
        self.mycountdown = cd.Countdown((0,0,0,0), sw.real_time)
        self.mytimer = sw.Stopwatch(sw.real_time)
        #convert countdown_time (which is in seconds (this happens automatically when initializing a countdown)) to a tuple
        self.countdown_time = self.mytimer.convert_time(self.mycountdown.countdown_time)
        self.root = tk.Tk()
        self.root.title("Countdown")
        
        self.on_state = False
        
        self.textvar = tk.StringVar()
        
        self.new_output = (00,00,00)
      
        self.output = "{:02d}:{:02d}:{:02d}".format(self.countdown_time[0], self.countdown_time[1], self.countdown_time[2])
        self.textvar.set(self.output)
        self.label = tk.Label(textvariable=self.textvar, font=("Arial",16)).grid(row=0, column=0)
        
        self.small_text = tk.StringVar()
        self.small_output = "000"
        self.small_text.set(self.small_output)
        self.small_label = tk.Label(textvariable=self.small_text, width=5, font=("Arial",8)).grid(row=0, column=0, sticky="e")
      
        self.frame = frame = tk.Frame(self.root)
        frame.grid()
        
        self.start_button = tk.Button(frame, text="START", fg="green", width=5, command=self.start)
        self.start_button.grid(row=1, column=0)
        
        #self.stop_button = tk.Button(frame, text="STOP", fg="red", width=5, command=self.stop)
        #self.stop_button.grid(row=1, column=1)
        self.reset_button = tk.Button(frame, text="RESET", fg="orange", width=5, command=self.reset)
        self.reset_button.grid(row=1, column=1)
        self.quit_button = tk.Button(frame, text="QUIT", width=5, command = self.root.quit)
        self.quit_button.grid(row=1, column=2)
        
        self.time_left = 0
        
        #lf = tk.LabelFrame(self.root, text="Keypad", bd=3, 
        #                   relief=tk.RIDGE).grid(columnspan=3)
        self.button_list = [
        '1','2','3',
        '4','5','6',
        '7','8','9',
        '0']
        row = 2
        column = 0
        n = 0
        number_button = list(range(len(self.button_list)))
        for label in self.button_list:
            button_command = partial(self.callback, label)
            number_button[n] = tk.Button(self.frame, text=label, width=5, command=button_command)
            number_button[n].grid(row=row, column=column)
            n += 1
            column += 1
            if column > 2:
                column = 0
                row +=1
            if n == 9:
                column = 1
        self.click_counter = 0
        self.reset_counter = 0
                
    def callback(self, label):
        print "Click {}".format(self.click_counter)
        # "hh:mm:ss" -> [h,h,m,m,s,s]
        self.new_output = convert_time_input(self.output)
        # take off first element in new_output, and add label to the end
        self.new_output.pop(0)
        self.new_output.append(label)
        
        #count up 1
        self.click_counter += 1
        
        if self.click_counter > 6:
            self.output = self.new_output
            self.reset()
            return
        
        #[h,h,m,m,s,s] -> (hh,mm,ss, ms (always zero))
        self.new_output = revert_time_input(self.new_output)
        
        
        
        self.output = "{:02d}:{:02d}:{:02d}".format(self.new_output[0], self.new_output[1], self.new_output[2])
        self.textvar.set(self.output)
    
        return self.output
             
        

    def print_elapsed(self):
        if self.on_state:
    
            self.time_left = self.mytimer.format_time(self.mytimer.convert_time(self.mycountdown.time_remaining()))
            
            self.output = self.time_left[0]
            
            self.small_output = self.time_left[1]
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
            
            #print "this is the time remaining {}" .format(self.mycountdown.time_remaining())
            
            if self.mycountdown.time_remaining() < 0:
                self.stop()
                if self.start_button.winfo_ismapped():
                    self.start_button.grid_forget()
                
            self.root.after(50, self.print_elapsed)
            
            
        else:
            
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
        
        
        
    def start(self):
        print "this is the new_output {}".format(self.new_output)
        #change the countdown_time in the countdown instance
        self.mycountdown.input_countdown_time(self.new_output)
        
        #change the countdown_Time for the Cdapp instance
        self.countdown_time = self.mytimer.convert_time(self.mycountdown.countdown_time)
        
        
        print "this is the time remaining{}".format(self.mycountdown.time_remaining())
        if self.mycountdown.time_remaining() <= 0:
            raise RuntimeError('Time remaining is zero, input a countdown time')
            
            
        
            
        if not self.on_state:
            self.on_state = True
            self.mycountdown.start_countdown()
            self.print_elapsed()
            self.start_button.config(text = "PAUSE")
            
        else:
            self.on_state = False
            self.mycountdown.stop_countdown()
            self.start_button.config(text = "START")
            
        
    def stop(self):
        self.mycountdown.stop_countdown()
        self.on_state = False
        self.print_elapsed()
        self.output = "00:00:00"
        self.small_output = "000"
        self.textvar.set(self.output)
        self.small_text.set(self.small_output)
        return
        
        
    def reset(self):
        print "timer is being reset"
        if self.reset_counter >= 1:
            self.reset_counter = 0
            self.mycountdown.countdown_time = 0
            
        self.reset_counter += 1
        self.start_button.grid(row=1, column=0)

        self.mycountdown.reset_countdown()
        self.countdown_time = self.mytimer.convert_time(self.mycountdown.countdown_time)
        self.on_state = False
        self.start_button.config(text = "START")
        self.click_counter = 0
        self.output = "{:02d}:{:02d}:{:02d}".format(self.countdown_time[0], self.countdown_time[1], self.countdown_time[2])
        self.small_output = "000"
        self.new_output = convert_time_input(self.output)
        self.new_output = revert_time_input(self.new_output)
        self.print_elapsed()
        print "here is output after being reset {}".format(self.output)
        
   
def main():
    """Run main."""
    
    a = Cdapp()
    a.root.mainloop()

    return 0

if __name__ == '__main__':
    main()
