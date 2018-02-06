
#this fuction test for the type of value; is it an integer, a string or a list.  then depenidng on it's value prints a message

def filterByType(item):
    if type(item) == int:
        if item >= 100:
            print "That's a big number!"
        else:
            print "That's a small number." 
    elif type(item) == str:
        if len(item) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    else:
        if len(item) >= 10:
            print "Big List!"
        else:
            print "Short List"
  
  
filterByType([1,7,4,21])
filterByType(45)
filterByType("Rubber baby buggy bumpers")