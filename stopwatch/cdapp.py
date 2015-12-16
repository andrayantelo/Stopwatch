import countdown as cd
import stopwatch as st
import time

def convert_time(self, time):
        """Takes a time given in hh:mm:ss:ms format and returns the number
        of seconds it corresponds to.
        Parameters:
            time: tuple format (hh, mm, ss, ms) 
        """
        if len(time) != 4:
            raise RuntimeError("time tuple is not of length 4")
        hours = time[0]*3600
        minutes = time[1]*60
        sec = time[2]
        millisec = time[3]*.001
        
        total = hours + minutes + sec + millisec
        return total
