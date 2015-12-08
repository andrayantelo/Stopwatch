from nose.tools import *
from stopwatch.stopwatch import *
import unittest

def make_fake_time_function(test_numbers):
    nums = iter(test_numbers)
    def fake_time():
        return nums.next()
    return fake_time
    
class TestStopwatch(unittest.TestCase):
    
    def setUp(self):
        self.mytimer = Stopwatch(real_time)
        self.epsilon = 0.1
    
    def test_repr(self):
        assert_equal(self.mytimer.__repr__(), "Stopwatch()")
    
    def test_init(self):
        assert_equal(self.mytimer._stop_time, 0)
        assert_equal(self.mytimer.elapsed_time, 0)
        assert_equal(self.mytimer._start_time, 0)
        
    def test_start_timer(self):
        self.mytimer.start_timer()
        then = self.mytimer._start_time
        now = time.time()
        time_diff = now - then
        assert_true(abs(time_diff < self.epsilon))
        assert_true(self.mytimer._start_state)
        
    def test_stop_timer(self):
        start = self.mytimer.start_timer()
        stop = self.mytimer.stop_timer()
        assert_true(self.mytimer._stop_time - self.mytimer._start_time < self.epsilon)
        assert_true(not self.mytimer._start_state)
        
    def test_convert_time(self):
        time_diff = 5410.002 #seconds
        time_diff = self.mytimer.convert_time(time_diff)
        assert_equal(time_diff, (1.0, 30.0, 10.0, 2.0 ))
        
    def test_format_time(self):
        time_min_sec = (0, 55, 45, 0)
        self.mytimer.format_time(time_min_sec)
        assert_equal(self.mytimer.format_time(time_min_sec), ("00:55:45", "000"))
        
    def test_elapsed(self):
        #test_timer = Stopwatch(time.time)
        #mytimer.start_timer()
        #mytimer.stop_timer()
        #assert_equal(0 <mytimer.elapsed() < self.epsilon, True)
        #mytimer.reset()
        self.mytimer.start_timer()
        assert_equal(self.mytimer._start_state, True)
        assert_equal(abs(self.mytimer.elapsed() - (time.time() - self.mytimer._start_time) < self.epsilon), True)
        mytimer.resert()
        
        
    def test_reset(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        self.mytimer.reset()
        assert_equal(self.mytimer._start_time, 0)
        assert_equal(self.mytimer._stop_time, 0)
        assert_equal(self.mytimer.elapsed_time, 0)
        
        
        


