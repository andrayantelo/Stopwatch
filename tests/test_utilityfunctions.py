#utilityfunctions testing module
import nose.tools as nt
import unittest
import stopwatch.utilityfunctions as uf
import Tkinter as tk
import cdapp as ca

class TestUtilityfunctions(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_seconds_to_tuple(self):
        time_diff = 5410.001 #seconds
        time_diff = uf.seconds_to_tuple(time_diff)
        
        nt.assert_equal(time_diff, (1.0, 30.0, 10.0, 1))
        
        
    def test_tuple_to_seconds(self):
        time_diff = (1.0, 30.0, 10.0, 1)
        time_diff = uf.tuple_to_seconds(time_diff)
        
        nt.assert_equal(time_diff, 5410.001)
        nt.assert_raises(TypeError, uf.tuple_to_seconds, 15)
        
    def test_tuple_to_clockface(self):
        time_min_sec = (0, 55, 45, 1)
        
        uf.tuple_to_clockface(time_min_sec)
        
        nt.assert_equal(uf.tuple_to_clockface(time_min_sec), ("00:55:45", "001"))
        
    def test_hide_me(self):
        root = tk.Tk()
        frame = tk.Frame(root)
        test_button = tk.Button(frame)
        test_button.pack()
        
        """ Can use the following:
        root = tk.Tk()
        w = Label(root, text="hello")
        w.pack()
        w.winfo_ismapped()
        w.pack_forget()
        w.winfo_ismapped() """
        
        
