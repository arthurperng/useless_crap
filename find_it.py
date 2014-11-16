from random import *
a = randint(1, 20)
b = randint(1, 20)
for x in range(1, 21, 1):
    for y in range(1, 21, 1):
        if x==a and y==b:
            print 4,
        else:
             print "A",
    print
x = raw_input("type anything if you want to move on.")
a = randint(1, 40)
b = randint(1, 40)
for x in range(1, 41, 1):
    for y in range(1, 41, 1):
        if x==a and y==b:
            print 0,
        else:
             print "O",
    print
x = raw_input("type anything if you want to move on.")
a = randint(1, 60)
b = randint(1, 60)
for x in range(1, 61, 1):
    for y in range(1, 61, 1):
        if x==a and y==b:
            print 5,
        else:
             print "S",
    print
x = raw_input("type anything if you want to move on.")
a = randint(1, 80)
b = randint(1, 80)
for x in range(1, 81, 1):
    for y in range(1, 81, 1):
        if x==a and y==b:
            print 1,
        else:
             print "l",
    print


