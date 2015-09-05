from nose.tools import *
from stopwatch.stopwatch import *


def test_repr():
    mytimer = Stopwatch()
    assert_equal(mytimer.__repr__(), "stopwatch()")
    
def test_start_timer():
    mytimer = Stopwatch()
    pass
    
