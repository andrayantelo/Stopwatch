from nose.tools import *
from stopwatch.stopwatch import *
import unittest

class TestStopwatch(unittest.TestCase):
    
    def setUp(self):
        self.mytimer = Stopwatch()
        self.epsilon = 0.1
    
    def test_repr(self):
        assert_equal(self.mytimer.__repr__(), "Stopwatch()")
    
    def test_init(self):
        mytimer = self.mytimer
        assert_equal(mytimer._stop_time, 0)
        assert_equal(mytimer.elapsed_time, 0)
        assert_equal(mytimer._start_time, 0)
        
    def test_start_timer(self):
        then = self.mytimer.start_timer()
        then = self.mytimer._start_time
        now = time.time()
        time_diff = now - then
        assert_true(abs(time_diff < self.epsilon))
        
    def test_stop_timer(self):
        start = mytimer.start_timer()
        stop = mytimer.stop_timer()
        assert_true(mytimer._stop_time - mytimer._start_time < self.epsilon)
        
    def test_convert_time(self):
        time_diff = 5410.002 #seconds
        time_diff = mytimer.convert_time(time_diff)
        assert_equal(time_diff, (1.0, 30.0, 10.0, 2.0 ))
        
    def test_format_time(self):
        time_min_sec = (55, 45)
        mytimer.format_time(time_min_sec)
        assert_equal(mytimer.format_time(time_min_sec), "55:45")
        
    def test_elapsed(self):
        mytimer.start_timer()
        time.sleep(1)
        mytimer.stop_timer()
        assert_equal(mytimer.elapsed() <= 1 + self.epsilon, True)
        
        
        


