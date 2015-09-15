from nose.tools import *
from stopwatch.stopwatch import *
import unittest

class TestStopwatch(unittest.TestCase):
    
    def setUp(self):
        self.mytimer = Stopwatch()
    
    def test_repr(self):
        assert_equal(self.mytimer.__repr__(), "Stopwatch()")
    
    def test_init(self):
        mytimer = self.mytimer
        assert_equal(mytimer.pause_state , False)
        assert_equal(mytimer.time_of_pause, 0)
        assert_equal(mytimer.stop_time, 0)
        assert_equal(mytimer.pause_duration, 0)
        assert_equal(mytimer.elapsed_time, 0)
        
    def test_start_timer(self):
        then = self.mytimer._start_timer()
        time.sleep(1)
        now = time.time()
        time_diff = now - then
        assert_equal(round(time_diff, 2), 1)
        
    def test_stop_timer(self):
        start = mytimer._start_timer()
        time.sleep(1)
        stop = mytimer._stop_timer()
        time_diff = stop - start
        epsilon = 0.1
        assert_equal(time_diff < epsilon, True)
        


