my_list = ["love", "peace"]
if all(type(n) is str for n in my_list) == True:
    print "All strings", my_list
    #print sum(my_list), "love"
else:
    print "not all integers"
