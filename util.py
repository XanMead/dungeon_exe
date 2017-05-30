import datetime

def theTime():
    """Returns h:m:s"""
    now = datetime.datetime.now()
    return '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

def helloTime():
    return "Hello! The time is " + theTime() + "!"

print(theTime())
