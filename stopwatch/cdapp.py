import countdown as cd
import stopwatch as sw
import time
import Tkinter as tk

#    def convert_time(self, time):
#        """Takes a time given in hh:mm:ss:ms format and returns the number
#        of seconds it corresponds to.
#        Parameters:
#            time: tuple format (hh, mm, ss, ms) 
#        """
#        if len(time) != 4:
#            raise RuntimeError("time tuple is not of length 4")
#        hours = time[0]*3600
#        minutes = time[1]*60
#        sec = time[2]
#        millisec = time[3]*.001
        
#        total = hours + minutes + sec + millisec
#        return total

        
class Cdapp(object):
    def __init__(self):
        self.mycountdown = cd.Countdown((0,0,3,0), sw.real_time)
        self.mytimer = sw.Stopwatch(sw.real_time)
        #countdown_time as a tuple
        self.countdown_time = self.mytimer.convert_time(self.mycountdown.countdown_time)
        self.root = tk.Tk()
        self.root.title("Countdown")
        
        self.on_state = False
        
        self.textvar = tk.StringVar()
        print self.countdown_time
        self.output = "{:02d}:{:02d}:{:02d}".format(int(self.countdown_time[0]), int(self.countdown_time[1]), int(self.countdown_time[2]))
        self.textvar.set(self.output)
        self.label = tk.Label(textvariable=self.textvar, font=("Arial",16)).grid(row=0, column=0)
        
        self.small_text = tk.StringVar()
        self.small_output = "000"
        self.small_text.set(self.small_output)
        self.small_label = tk.Label(textvariable=self.small_text, width=5, font=("Arial",8)).grid(row=0, column=0, sticky="e")
      
        self.frame = frame = tk.Frame(self.root)
        frame.grid()
        
        self.start_button = tk.Button(frame, text="START", fg="green", command=self.start).grid(row=1, column=0)
        self.stop_button = tk.Button(frame, text="STOP", fg="red", command=self.stop).grid(row=1, column=1)
        self.reset_button = tk.Button(frame, text="RESET", fg="orange", command=self.reset).grid(row=1, column=2)
        
        self.time_left = 0

    def print_elapsed(self):
        if self.on_state == True:
    
            self.time_left = self.mytimer.format_time(self.mytimer.convert_time(self.mycountdown.time_remaining()))
            self.output = self.time_left[0]
            self.small_output = self.time_left[1]
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
            
            #print "this is the time remaining {}" .format(self.mycountdown.time_remaining())
            
            if self.mycountdown.time_remaining() < 0:
                self.stop()
                
            self.root.after(50, self.print_elapsed)
            
            
        else:
            
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
        
    def start(self):
        self.mycountdown.start_countdown()
        self.on_state = True
        self.print_elapsed()
        
        
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
        self.mycountdown.reset_countdown()
        self.on_state = False
        self.output = "00:00:00"
        self.small_output = "000"
        self.print_elapsed()
        
   
def main():
    """Run main."""
    
    a = Cdapp()
    a.root.mainloop()

    return 0

if __name__ == '__main__':
    main()
