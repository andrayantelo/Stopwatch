import nose.tools as nt
import stopwatch.stopwatch as sw
import unittest
import time

def make_fake_time_function(test_numbers):
    nums = iter(test_numbers)
    def fake_time():
        return nums.next()
    return fake_time
    
fake_time = make_fake_time_function(range(10000))
    
class TestStopwatch(unittest.TestCase):
    
    def setUp(self):
        self.mytimer = sw.Stopwatch(fake_time)
        self.epsilon = 0.1
    
    def test_repr(self):
        nt.assert_equal(self.mytimer.__repr__(), "Stopwatch()")
    
    def test_init(self):
        nt.assert_equal(self.mytimer._stop_time, 0)
        nt.assert_equal(self.mytimer.elapsed_time, 0)
        nt.assert_equal(self.mytimer._start_time, 0)
        
    def test_start_timer(self):
        self.mytimer.start_timer()
        print self._start_time 
        nt.assert_equal(self.mytimer._start_time, 0)
        nt.assert_equal(self.mytimer._start_state)
        
    def test_stop_timer(self):
        start = self.mytimer.start_timer()
        nt.assert_equal(self.mytimer._start_time, 1)
        stop = self.mytimer.stop_timer()
        nt.assert_equal(self.mytimer._stop_time - self.mytimer._start_time, 1)
        nt.assert_equal(not self.mytimer._start_state)
        
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
        nt.assert_equal(self.mytimer._start_state, True)
        nt.assert_equal(abs(self.mytimer.elapsed() - (time.time() - self.mytimer._start_time) < self.epsilon), True)
        
        self.mytimer.reset()
        
        self.mytimer.start_timer() 
        time.sleep(1)
        self.mytimer.stop_timer()
        first_elapsed = self.mytimer.elapsed()
        nt.assert_equal(abs(self.mytimer.elapsed() - (time.time() - self.mytimer._start_time) < self.epsilon), True)
        self.mytimer.start_timer()
        time.sleep(1)
        self.mytimer.stop_timer()
        second_elapsed = self.mytimer.elapsed()
        print second_elapsed
        print first_elapsed
        nt.assert_equal(second_elapsed > first_elapsed)
        
        self.mytimer.reset()
        
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        time.sleep(2)
        self.mytimer.start_timer()
        self.mytimer.elapsed()
        time.sleep(2)
        self.mytimer.elapsed()
        #print self.mytimer.elapsed()  
        nt.assert_equal(abs(self.mytimer.elapsed() - 2) < self.epsilon)
    
        
        
        
        
        
        
    def test_reset(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        self.mytimer.reset()
        nt.assert_equal(self.mytimer._start_time, 0)
        nt.assert_equal(self.mytimer._stop_time, 0)
        nt.assert_equal(self.mytimer.elapsed_time, 0)
        
        
        


