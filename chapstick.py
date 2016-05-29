import sys

def normal(a):
    x = 0 if a[0]>4 else a[0]
    y = 0 if a[1]>4 else a[1]
    if x < y:
        return (y,x)
    return (x,y)

def lose(a):
    return a==(0,0)

def split(a,b):
    if a[1] ==0:
        return set()
    answer = set()
    s = a[0] + a[1]
    for x in range(1, s+1):
        y = s-x
        n = normal((x,y))
        if (not lose(n)) and (not n == a):
            answer.add((n,b))
    return answer
    
def hit(a,b):
    answer = set()
    for i in range(2):
        for j in range(2):
            n = [b[0], b[1]]
            if n[j]>0:
                n[j] += a[i]
                nn =normal(n)
                if nn!=b and n[1]>=n[0]:
                    answer.add((a,nn))
                
    return answer

def revert_set(xx):
    return set([(x[1], x[0]) for x in xx])

def print_states(s):
    for state in s:
        print '',state

all_hands = [(i,j) for i in range(1,5) for j in range(i+1)] 


stop = False
certain_lose = set([((0,0), h) for h in all_hands])
certain_win = set([(b,a) for (a,b) in certain_lose])
unknown_states = set([(a,b) for a in all_hands for b in all_hands if (a,b) not in certain_lose and (a,b) not in certain_win])
print 'certain_lose'
print_states(certain_lose)

iter = 0
while not stop:
    iter += 1
    stop = True
    new_wins = set()
    new_loss = set()
    for (a,b) in unknown_states:
        print "*", (a,b)
        all_outcome = revert_set(split(a,b) | hit(a,b))
        print 'all_outcome', all_outcome
        # one way to make opponent certain lose, then it's certain_win
        wins =  all_outcome & certain_lose
        #print 'wins', wins
        if wins:
            print 'wins', wins
            stop = False
            new_wins.add((a,b))
        # if every outcome make opponent certain win, then it's certain_loss
        if all_outcome.issubset(certain_win):
            print 'lose'
            stop = False
            #print 'add new_loss', (a,b)
            new_loss.add((a,b))
        #print 'new_wins', (new_wins)
        #print 'new_loss', (new_loss)
    if not stop:
        print 'Iteration', iter, "Win:"
        print (new_wins)    
        print 'Iteration', iter, "Lose:"
        print (new_loss)    
    if (a,b) == ((1, 0), (4, 4)):
        print '--------------------'
        print all_outcome
        print wins
        
    certain_win = certain_win.union(new_wins)
    certain_lose = certain_lose.union(new_loss)
    unknown_states = set([(a,b) for a in all_hands for b in all_hands if (a,b) not in certain_lose and (a,b) not in certain_win])
            

#print certain_win
#print certain_lose
            