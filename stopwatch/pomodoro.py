import stopwatch as sw
import countdown as cd
import time


class Pomodoro(object):
    
    def __init__(self, work_time, break_time):
        self.work_countdown = cd.Countdown(work_time, sw.real_time)
        self.break_countdown = cd.Countdown(break_time, sw.real_time)
        self.rounds_before_break = 4
        self.current_round = 0
        
    def advance_round(self):
        
        self.current_round += 1
        if self.current_round >= self.rounds_before_break:
            self.current_round = 0
            
    @property 
    def active_countdown(self):
        if self.current_round %2 == 0:
            return self.work_countdown
        else:
            return self.break_countdown
            
    def start_pomodoro(self):
        self.active_countdown.start_countdown()
        
    def stop_pomodoro(self):
        self.active_countdown.stop_countdown()
        
    def time_remaining(self):
        return self.active_countdown.time_remaining()
        
    def reset_pomodoro(self):
        self.work_countdown.reset()
        self.break_countdown.reset()
        self.current_round = 0
        self.active_countdown()
        
    def input_times(self, work_time, break_time):
        """Change the work and break times"""
        self.work_countdown.input_countdown_time(work_time)
        self.break_countdown.input_countdown_time(break_time)
        
        
        
        
        
    
