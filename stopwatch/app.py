from Tkinter import *
from stopwatch import *


class App(object):
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Stopwatch")
        
        self.on_state = True
        
        self.textvar = StringVar()
        self.output = "00:00:00"
        self.textvar.set(self.output)
        self.label = Label(textvariable=self.textvar, font=("Arial",16)).grid(row=0, column=0)
        
        self.small_text = StringVar()
        self.small_output = "000"
        self.small_text.set(self.small_output)
        self.small_label = Label(textvariable=self.small_text, width=5, font=("Arial",8)).grid(row=0, column=0, sticky="e")
      
        self.frame = frame = Frame(self.root)
        frame.grid()
        
        self.start_button = Button(frame, text="START", fg="green", command=self.start).grid(row=1, column=0)
        self.stop_button = Button(frame, text="STOP", fg="red", command=self.stop).grid(row=1, column=1)
        self.reset_button = Button(frame, text="RESET", fg="orange", command=self.reset).grid(row=1, column=2)

    def print_elapsed(self):
        if self.on_state == True: 
            self.time_elapsed = mytimer.format_time(mytimer.convert_time(mytimer.elapsed()))
            print self.time_elapsed
            self.output = self.time_elapsed[0]
            self.small_output = self.time_elapsed[1]
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
            
            
            self.root.after(50, self.print_elapsed)
            
        elif self.on_state == False:
            self.textvar.set(self.output)
            self.small_text.set(self.small_output)
        
    def start(self):
        mytimer.start_timer()
        self.on_state = True
        self.print_elapsed()
        
        
    def stop(self):
        mytimer.stop_timer()
        self.on_state = False
        self.print_elapsed()
        
        
    def reset(self):
        mytimer.reset()
        self.on_state = False
        self.output = "00:00:00"
        self.small_output = "000"
        self.print_elapsed()
        
   
def main():
    """Run main."""
    
    a = App()
    a.root.mainloop()

    return 0

if __name__ == '__main__':
    main()
    
