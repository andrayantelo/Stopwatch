import nose.tools as nt
import stopwatch.stopwatch as sw
import stopwatch.countdown as cd
import unittest
import time

def make_fake_time_function(test_numbers):
    nums = iter(test_numbers)
    def fake_time():
        return nums.next()
    return fake_time
    

    
class TestStopwatch(unittest.TestCase):
    
    def setUp(self):
        self.fake_time = make_fake_time_function(range(10000))
        self.mytimer = sw.Stopwatch(self.fake_time)
    
    def test_init(self):
        nt.assert_equal(self.mytimer._stop_time, 0)
        nt.assert_equal(self.mytimer.elapsed_time, 0)
        nt.assert_equal(self.mytimer._start_time, None)
        nt.assert_equal(self.mytimer._now, self.fake_time)
        nt.assert_equal(self.mytimer.elapsed(), 0)
        
    def test_start_timer(self):
        self.mytimer.start_timer()
        
        nt.assert_equal(self.mytimer._start_time, 0)
        nt.assert_true(self.mytimer._start_time is not None)
        nt.assert_raises(RuntimeError, self.mytimer.start_timer)
        
    def test_stop_timer(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        nt.assert_equal(self.mytimer._stop_time, 1)
        nt.assert_true(self.mytimer._start_time is None)
        nt.assert_equal(self.mytimer.elapsed(), 1)
        
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        nt.assert_equal(self.mytimer.elapsed(), 2)
        nt.assert_raises(RuntimeError, self.mytimer.stop_timer)
               
    def test_convert_time(self):
        time_diff = 5410.002 #seconds
        time_diff = self.mytimer.convert_time(time_diff)
        
        nt.assert_equal(time_diff, (1.0, 30.0, 10.0, 2.0 ))
        
    def test_format_time(self):
        time_min_sec = (0, 55, 45, 0)
        
        self.mytimer.format_time(time_min_sec)
        
        nt.assert_equal(self.mytimer.format_time(time_min_sec), ("00:55:45", "000"))
        
    def test_elapsed(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        nt.assert_equal(self.mytimer.elapsed(), 1)
        
        self.mytimer.start_timer()
        
        nt.assert_equal(self.mytimer.elapsed(), 2)
        nt.assert_equal(self.mytimer.elapsed(), 3)
        
        self.mytimer.stop_timer()
        
        nt.assert_equal(self.mytimer.elapsed(), 4)
        
    def test_reset(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        nt.assert_equal(self.mytimer.elapsed(), 2)
        nt.assert_equal(self.mytimer._start_time, None)
        nt.assert_equal(self.mytimer._stop_time, 3)
        
        self.mytimer.reset()
        
        nt.assert_equal(self.mytimer._start_time, None)
        nt.assert_equal(self.mytimer._stop_time, 0)
        nt.assert_equal(self.mytimer.elapsed_time, 0)
        
"""class TestCountdown(unittest.TestCase):
    
    def setUp(self):
        self.fake_time = make_fake_time_function(range(10000))
        self.countdown = cd.Countdown(10)
        
    def test_init(self):
        nt.assert_true(isinstance(self.countdown.timer, sw.Stopwatch))
        
    def test_start_countdown(self):
        pass
        
    def test_stop_countdown(self):
        pass
        
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

        
if __name__ == '__main__':
    unittest.main()
"""

