import nose.tools as nt
import stopwatch.stopwatch as sw
import stopwatch.countdown as cd
import unittest
import time

class TestCountdown(unittest.TestCase):
    
    def setUp(self):
        self.fake_time = sw.make_fake_time_function(range(10000))
        self.countdown = cd.Countdown(10)
        
    def test_init(self):
        nt.assert_true(isinstance(self.countdown.timer, sw.Stopwatch))
        nt.assert_equal(self.countdown.countdown_time, 10)
        
    def test_start_countdown(self):
        self.countdown.start_countdown()
        nt.assert_true(self.countdown.timer.running)
        
    def test_stop_countdown(self):
        with nt.assert_raises(RuntimeError):
            self.countdown.stop_countdown()
        self.countdown.start_countdown()
        self.countdown.stop_countdown()
        nt.assert_false(self.countdown.timer.running)
        
    def test_time_remaining(self):
        pass
        
    def test_reset_countdown(self):
        pass
        
    def test_input_countdown_time(self):
        pass
        
    def test_enter(self):
        pass
        
    def test_exit(self):
        pass
