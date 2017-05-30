import datetime

def theTime():
    """Returns h:m:s"""
    now = datetime.datetime.now()
    return '%s:%s:%s' % (now.hour, now.minute, now.second)

def helloTime():
    return "Hello! The time is " + theTime() + "!"

