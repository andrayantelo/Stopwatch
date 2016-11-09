import stopwatch.stopwatch as sw
import unittest as ut
import time
import stopwatch.utilityfunctions as uf

#see if you can use the with statement in here
#look up and understand unittest
#look up and understand nose.tools

class TestStopwatch(ut.TestCase):
    
    def setUp(self):
        self.fake_time = uf.make_fake_time_function(range(10000))
        self.mytimer = sw.Stopwatch(self.fake_time)
    
    def test_init(self):
        ut.assertEqual(self.mytimer._stop_time, 0)
        ut.assertEqual(self.mytimer.elapsed_time, 0)
        ut.assertEqual(self.mytimer._start_time, None)
        ut.assertEqual(self.mytimer._now, self.fake_time)
        ut.assertEqual(self.mytimer.elapsed(), 0)
        
    def test_start_timer(self):
        self.mytimer.start_timer()
        
        ut.assertEqual(self.mytimer._start_time, 0)
        ut.assertTrue(self.mytimer._start_time is not None)
        ut.assertRaises(RuntimeError, self.mytimer.start_timer)
        
    def test_stop_timer(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        ut.assertEqual(self.mytimer._stop_time, 1)
        ut.assertTrue(self.mytimer._start_time is None)
        ut.assertEqual(self.mytimer.elapsed(), 1)
        
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        ut.assertEqual(self.mytimer.elapsed(), 2)
        ut.assertRaises(RuntimeError, self.mytimer.stop_timer)
        
    def test_elapsed(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        ut.assertEqual(self.mytimer.elapsed(), 1)
        
        self.mytimer.start_timer()
        
        ut.assertEqual(self.mytimer.elapsed(), 2)
        ut.assertEqual(self.mytimer.elapsed(), 3)
        
        self.mytimer.stop_timer()
        
        ut.assertEqual(self.mytimer.elapsed(), 4)
        
    def test_reset(self):
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        self.mytimer.start_timer()
        self.mytimer.stop_timer()
        
        ut.assertEqual(self.mytimer.elapsed(), 2)
        ut.assertEqual(self.mytimer._start_time, None)
        ut.assertEqual(self.mytimer._stop_time, 3)
        
        self.mytimer.reset()
        
        ut.assertEqual(self.mytimer._start_time, None)
        ut.assertEqual(self.mytimer._stop_time, 0)
        ut.assertEqual(self.mytimer.elapsed_time, 0)
        
if __name__ == '__main__':
    unittest.main()


