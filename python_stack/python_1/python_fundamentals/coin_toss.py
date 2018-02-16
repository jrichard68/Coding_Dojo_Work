def coin_toss():
    import random
    heads = 0
    tails = 0
    for x in range(1, 5000):
        coin = random.randint(1,2)
        if coin == 1:
            heads +=1
            print "Attempt #", x,": Throwing a coin... It's heads!  ... You have", heads, "heads so far and", tails, "tails so far"
        else:
            tails +=1
            print "Attempt #", x,": Throwing a coin... It's heads!  ... You have", heads, "heads so far and", tails, "tails so far"

coin_toss()
