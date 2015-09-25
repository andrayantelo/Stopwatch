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
        self.label = Label(textvariable=self.textvar, font=("Arial",16)).grid(row=1,column=1)
        #self.label.pack()
        
        self.small_text = StringVar()
        self.small_output = "000"
        self.small_text.set(self.small_output)
        self.small_label = Label(textvariable=self.small_text, font=("Arial",8)).grid(row=3, column=2)
        #self.milliseconds.pack()
        
        frame = Frame(self.root)
        frame.grid(row=2)
        
        self.start_button = Button(frame, text="START", fg="green", command=self.start)
        self.start_button.grid(row=2, column=1)
        self.stop_button = Button(frame, text="STOP", fg="red", command=self.stop)
        self.stop_button.grid(row=2, column=2)
        self.reset_button = Button(frame, text="RESET", fg="yellow", command=self.reset)
        self.reset_button.grid(row=2, column=3)
        
        self.display_button = Button(frame, text="display", fg="blue", command=self.print_elapsed)
        self.display_button.grid(row=2, column=4)
        
        
        
        
    def print_elapsed(self):
        if self.on_state == True: 
            self.time_elapsed = mytimer.format_time(mytimer.convert_time(mytimer.elapsed()))
            
            self.output = self.time_elapsed[0]
            self.textvar.set(self.output)
            
            self.small_output = self.time_elapsed[1]

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
        self.on_state = False
        self.print_elapsed()
        
    def reset(self):
        self.on_state = False
        self.output = "00:00:00"
        self.print_elapsed()
        
        
    
app = App()

app.root.mainloop()
app.root.destroy()
