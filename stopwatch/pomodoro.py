import stopwatch as sw
import countdown as cd
import time


#NEED TO FIX THE ADVANCE ROUND FEATURE

class Pomodoro(object):
    
    def __init__(self):
        self.work_countdown = cd.Countdown(sw.real_time)
        self.break_countdown = cd.Countdown(sw.real_time)
        self.rounds_before_break = 4
        self.current_round = 0
        
        #set work countdown as default
        self._active_countdown = self.work_countdown
        
    def advance_round(self):
        
        self.current_round += 1
        if self.current_round >= self.rounds_before_break:
            self.current_round = 0
            
    @property 
    def active_countdown(self):
        return self._active_countdown
    
    @active_countdown.setter
    def active_countdown(self, active_countdown):
        if type(active_countdown) != cd.Countdown:
            raise TypeError('input must be an instance of Countdown')
        self._active_countdown = active_countdown
        
    def start_pomodoro(self):
        self.active_countdown.start_countdown()
        
    def stop_pomodoro(self):
        self.active_countdown.stop_countdown()
        
    def time_remaining(self):
        return self.active_countdown.time_remaining()
        
    def reset_pomodoro(self):
        self.work_countdown.countdowntime = (0,0,0,0)
        self.break_countdown.countdowntime = (0,0,0,0)
        self.current_round = 0
        
    def input_times(self, work_time, break_time):
        """Change the work and break times"""
        self.work_countdown.countdowntime = work_time
        self.break_countdown.countdowntime = break_time
        
        
        
        
        
    
 
