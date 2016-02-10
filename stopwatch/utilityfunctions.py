#utility functions module

def make_fake_time_function(test_numbers):
    nums = iter(test_numbers)
    def fake_time():
        return nums.next()
    return fake_time
    
fake_time = make_fake_time_function(range(10000))

def seconds_to_tuple(clock_time):
        """ Returns a tuple containing the hours, minutes, seconds 
        of a time given in seconds.
        
        Parameters:
        clock_time: int
            the time, in seconds, to be converted.
        """
        
        if type(clock_time) == tuple and len(clock_time) == 3:
            return clock_time
        
        milliseconds = clock_time * 1000
        sec, milliseconds = divmod(round(milliseconds,2), 1000)
        minutes, sec = divmod(round(clock_time,2), 60)
        hours, minutes = divmod(round(minutes,2), 60)
        output = (int(hours), int(minutes), int(sec), milliseconds)
        
        return output
        
def tuple_to_seconds(time_tuple):
    """ Takes a tuple and converts it to time in seconds.
        
    Parameters:
    time_tuple: tupe
        tuple containing (hours, minutes, sec, milliseconds).
    {hh, mm, ss) -> sec
    """
    
    if type(time_tuple) != tuple:
        raise TypeError('Must input a tuple containing hh, mm, ss, ms')
            
    hour = time_tuple[0] * 3600
    minutes = time_tuple[1] * 60
    sec = time_tuple[2] 
    milliseconds = time_tuple[3] * 0.001
        
    return hour + minutes + sec + milliseconds
        
def tuple_to_clockface(clock_tuple):
    """ Returns tuple of the time in a (('hour:minutes:seconds'), ms) format.
        
    Parameters:
    clock_tuple: int
        tuple containing (hours, minutes, sec, ms).
    """
    
    formatted_time = "%02d:%02d:%02d" %(clock_tuple[0], clock_tuple[1], clock_tuple[2])
    formatted_milliseconds = "%03d" %clock_tuple[3]
        
    return (formatted_time, formatted_milliseconds)
    
def hide_me(event):
    """ Hides a tkinter widget."""
    event.pack_forget()

def string_to_list(time):
    """Takes a time given in hh:mm:ss format and returns a list
    ['h','h','m','m','s','s'].
    Parameters:
    time: string format 'hh:mm:ss' 
    """
    new_time = ''
    for letter in time:
        if letter != ':':
            new_time += letter
    new_time = list(new_time)
    if len(new_time) != 6:
        raise RuntimeError("Time list is not of length 6")

    return new_time
    
def list_to_tuple(time):
    """Takes a time list in ['h', 'h', 'm', 'm', 's', 's'] format and returns a tuple
    (hh, mm, ss, ms).
    Parameters:
    time: list format ['h','h','m','m','s','s']
    ['h','h','m','m','s','s'] -> (hh,mm,ss, ms), ms always equal to 00
    """
    new_time = ''
    for element in time:
        new_time += str(element)
    
    n = 2
    new_time = [new_time[i:i+n] for i in range(0, len(new_time), n)]
    new_time = tuple([int(i) for i in new_time])
    new_tuple = (new_time[0], new_time[1], new_time[2], 00)
        
    return new_tuple
