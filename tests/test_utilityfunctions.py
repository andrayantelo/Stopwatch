#utilityfunctions testing module
import nose.tools as nt
import unittest
import stopwatch.utilityfunctions as uf

class TestUtilityfunctions(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_seconds_to_tuple(self):
        time_diff = 5410 #seconds
        time_diff = self.mytimer.convert_time(time_diff)
        
        nt.assert_equal(time_diff, (1.0, 30.0, 10.0))
        
        
    def test_tuple_to_seconds(self):
        time_diff = (1.0, 30.0, 10.0)
        time_diff = self.mytimer.revert_time(time_diff)
        
        nt.assert_equal(time_diff, 5410)
        nt.assert_raises(TypeError, self.mytimer.revert_time, 15)
        
    def test_tuple_to_clockface(self):
        time_min_sec = (0, 55, 45, 0)
        
        self.mytimer.format_time(time_min_sec)
        
        nt.assert_equal(self.mytimer.format_time(time_min_sec), ("00:55:45", "000"))
