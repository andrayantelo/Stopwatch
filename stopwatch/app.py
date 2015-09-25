from Tkinter import *
from stopwatch import *


class App():
    def __init__(self, master):
        
        master.title("Stopwatch")
        frame = Frame(master)
        frame.pack()
        
        self.textvar = StringVar()
        self.textvar.set("00:00")
        self.label = Label(textvariable=self.textvar, font=16)
        self.label.pack(side=TOP)
        
        self.start_button = Button(frame, text="START", fg="green", command=mytimer.start_timer)
        self.start_button.pack(side=LEFT)
        self.stop_button = Button(frame, text="STOP", fg="red", command=mytimer.stop_timer)
        self.stop_button.pack(side=LEFT)
        self.reset_button = Button(frame, text="RESET", fg="yellow", command=mytimer.reset)
        self.reset_button.pack(side=LEFT)
        
        self.display_button = Button(frame, text="display", fg="blue", command=self.print_elapsed)
        self.display_button.pack(side=LEFT)
        
        
        
        
    def print_elapsed(self):
        print(mytimer.elapsed())
        
root = Tk()


app = App(root)

root.mainloop()
root.destroy()
