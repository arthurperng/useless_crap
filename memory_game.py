# Only works in console
from random import *
a=""
level=1
while True:
    x=chr(randint(33, 128))
    a+=x
    print '\033c'
    print "level ", level
    print "new character is", x
    b=raw_input("what is the string?")
    level+=1
    if b!=a:
        print "game over!"
        break
print "You got to level ", level-1
print chr(7)*1000000
print "The string was ", a




