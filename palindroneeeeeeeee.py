while True:
    steps=0
    x=raw_input("what will the number be?")
    while x!=x[::-1]:
        steps+=1
        y=str(x)[::-1]
        y=int(y)
        print x, y
        x=int(x)
        x+=y
        x=str(x)
    print "your palindrome is ", x
    print "it took ", steps, " steps"

