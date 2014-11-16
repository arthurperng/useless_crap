from random import *
import time
import sys
tiles=0
a=time.time()
goal=20
z=2
while True:
    print "Level up!"
    print "you now need to copy ", goal, "tiles"
    if z!=9:
        print "put your fingers on keys 1 through ", z
    goal+=10
    time.sleep(1)
    print "3"
    time.sleep(1)
    print "2"
    time.sleep(1)
    print "1"
    time.sleep(1)
    print "GO!"
    time.sleep(0.5)
    for i in range(1, goal):
        x=randint(1, z)
        y=raw_input(x)
        if int(y)!=x:
            print "game over!"
            sys.exit()
        tiles+=1
    b=time.time()
    z+=1
print "it took you ", b-a, "seconds"
print "you tapped ", tiles, "tiles"
print "your average pace was ", tiles/(b-a), "seconds per tile"