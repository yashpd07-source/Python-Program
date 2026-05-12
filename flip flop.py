def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = (3,4,5,5,6,6,5,4,33,)
if (palind(r)):
    print("The Tuple is Flip-Flop")
else:
    print("The Tuple is not Flip-Flop")
