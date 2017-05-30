import datetime
import random

def theTime():
    """Returns h:m:s"""
    now = datetime.datetime.now()
    return '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

def helloTime():
    return "Hello! The time is " + theTime() + "!"

def roll(dice):
    """Takes arguments in the format "{#}d{#}", e.g. 2d6 returns the total"""
    try:
        num, die = dice.split('d')
        total = 0
        for i in range(0,int(num)):
            roll = random.randint(1,int(die))
            print("rolling... " + str(roll))
            total += roll
        return total
    except Exception as e:
        print("Error: " + str(e))
        return "Something went wrong! Check your input."

