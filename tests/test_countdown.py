import nose.tools as nt
import stopwatch.stopwatch as sw
import stopwatch.countdown as cd
import unittest
import time

class TestCountdown(unittest.TestCase):
    
    def setUp(self):
        self.fake_time = sw.make_fake_time_function(range(10000))
        self.countdown = cd.Countdown((0, 0, 10, 0), sw.fake_time)
        
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
        self.countdown.start_countdown()
        self.countdown.stop_countdown()
        nt.assert_equal(self.countdown.time_remaining(), 9)
        self.countdown.start_countdown()
        self.countdown.stop_countdown()
        nt.assert_equal(self.countdown.time_remaining(), 8)
        
    def test_reset_countdown(self):
        self.countdown.start_countdown()
        self.countdown.stop_countdown()
        nt.assert_true(self.countdown.time_remaining() != 10)
        self.countdown.reset_countdown()
        nt.assert_equal(self.countdown.time_remaining(), 10)
        
        
    def test_input_countdown_time(self):
        nt.assert_equal(self.countdown.countdown_time, 10)
        self.countdown.input_countdown_time(15)
        nt.assert_equal(self.countdown.countdown_time, 15)
        
    def test_context_manager(self):
        with self.countdown:
            nt.assert_true(self.countdown.timer.running)
        nt.assert_false(self.countdown.timer.running)
        
if __name__ == '__main__':
    unittest.main()

