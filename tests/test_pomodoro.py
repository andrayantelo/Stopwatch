#pomodoro testing module

import nose.tools as nt
import stopwatch.stopwatch as sw
import unittest
import stopwatch.countdown as ct
import stopwatch.pomodoro as pom

class TestPomodoro(unittest.TestCase):
    
    def setUp(self):
        self.mypom = pom.Pomodoro()
        
    def test_init(self):
        nt.assert_true(isinstance(self.mypom.work_countdown, ct.Countdown))
        nt.assert_true(isinstance(self.mypom.break_countdown, ct.Countdown))
        nt.assert_equal(self.mypom.rounds_before_break, 4)
        nt.assert_equal(self.mypom.current_round, 0)
        
    def test_advance_round(self):
        self.mypom.advance_round()
        nt.assert_equal(self.mypom.current_round, 1)
        self.mypom.advance_round()
        nt.assert_equal(self.mypom.current_round, 2)
        self.mypom.advance_round()
        self.mypom.advance_round()
        nt.assert_equal(self.mypom.current_round, 0)
        
    def test_active_countdown(self):
        nt.assert_true(self.mypom.active_countdown, self.mypom.work_countdown)
        self.mypom.advance_round()
        nt.assert_true(self.mypom.active_countdown, self.mypom.break_countdown)
        
    def test_start_pomodoro(self):
        self.mypom.start_pomodoro()
        nt.assert_true(self.mypom.work_countdown.timer.running)
        with nt.assert_raises(RuntimeError):
            self.mypom.start_pomodoro()
        
    def test_stop_pomodoro(self):
        pass
        
    def test_time_remaining(self):
        pass
        
    def test_reset_pomodoro(self):
        pass
        
    def test_input_times(self):
        pass
    
