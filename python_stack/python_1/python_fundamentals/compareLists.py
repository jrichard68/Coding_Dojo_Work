def compareLists(list1, list2):
    if  set(list1) == set(list2):
        print "Lists are the same"
    else:
        print "List are not the same"
    

compareLists(['food','carrots','bread','milk'], ['celery','carrots','bread','milk'])