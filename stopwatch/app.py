from Tkinter import *
from stopwatch import *


class App():
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Stopwatch")
        
        self.on_state = True
        self.textvar = StringVar()
        self.output = "00:00:00"
        self.textvar.set(self.output)
        self.label = Label(textvariable=self.textvar, font=16)
        self.label.pack(side=TOP)
        
        frame = Frame(self.root)
        frame.pack()
        
        self.start_button = Button(frame, text="START", fg="green", command=self.start)
        self.start_button.pack(side=LEFT)
        self.stop_button = Button(frame, text="STOP", fg="red", command=self.stop)
        self.stop_button.pack(side=LEFT)
        self.reset_button = Button(frame, text="RESET", fg="yellow", command=mytimer.reset)
        self.reset_button.pack(side=LEFT)
        
        self.display_button = Button(frame, text="display", fg="blue", command=self.print_elapsed)
        self.display_button.pack(side=LEFT)
        
        
        
        
    def print_elapsed(self):
        if self.on_state == True: 
            self.output = mytimer.format_time(mytimer.convert_time(mytimer.elapsed()))
            self.textvar.set(self.output)
            self.root.after(1000, self.print_elapsed)
        elif self.on_state == False:
            self.textvar.set(self.output)
        
    def start(self):
        mytimer.start_timer()
        self.on_state = True
        self.print_elapsed()
        
    def stop(self):
        self.on_state = False
        self.print_elapsed()
        
    def reset(self):
        pass
        
        
    
app = App()

app.root.mainloop()
app.root.destroy()
