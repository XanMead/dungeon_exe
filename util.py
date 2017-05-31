import datetime
import random

def theTime():
    """Returns h:m:s"""
    now = datetime.datetime.now()
    return '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

def helloTime():
    return "%s The time is %s." % (randomGreeting(), theTime())

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

def randomGreeting():
    """returns a string containing a random greeting"""
    greetings = ["Hello!","Hello.","Hi!","Hi.","Hey!","Hey.","Bonjour!","Bonjour.","Salutations!","Salutations.","Hail and well met!","Hail and well met.","How are you today?","How are you today?","Shalom!","Shalom.","Salut!","Salut.","Greetings!","Greetings.","Hello World!","Hello World.","Oh, hi!","Oh, hi.","Guten tag!","Guten tag.","Thank you for listening!!","Thank you for listening!","Stay hydrated!!","Stay hydrated!","Remember to breathe!!","Remember to breathe!","Hi mom! @godelescherbabe.","I love you mom! @godelescherbabe.","I hope mom is proud of me! @godelescherbabe.","I know mom is proud of me! @godelescherbabe.","Good tidings upon you!","Good tidings upon you.","Are you sitting comfortably?","Are you sitting comfortably?","Remember to stretch!!","Remember to stretch!","Black Lives Matter!","Protect trans lives!","The president is a white supremacist!","This bot is a socialist <3"]
    return random.choice(greetings)
