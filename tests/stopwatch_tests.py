from nose.tools import *
from stopwatch.stopwatch import *
from datetime import timedelta


def test_repr():
    mytimer = Stopwatch()
    assert_equal(mytimer.__repr__(), "Stopwatch()")
    
def test_init():
    mytimer = Stopwatch()
    assert_equal(mytimer.pause_state , False)
    assert_equal(mytimer.time_of_pause, 0)
    assert_equal(mytimer.stop_time, 0)
    assert_equal(mytimer.pause_duration, 0)
    assert_equal(mytimer.elapsed_time, 0)
    
def test_start_timer():
    mytimer = Stopwatch()
    then = mytimer._start_timer()
    now = time.time()
    tdelta = now - then
    return tdelta


