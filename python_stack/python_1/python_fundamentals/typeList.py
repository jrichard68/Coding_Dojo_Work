def typeList(item):
    sum = 0
    newString = []
    count = 0
    while count < len(item):
        if type(item[count]) == int:
            sum = sum + item[count]
            count +=1
        else:
            newString.append(item[count])
            count +=1
    if all(type(n) is int for n in item) == True:
        print "The list you entered is of integer type."
        print "Sum: ", sum
    else:
        print "The list you entered is of string type."
        print "String: ", newString

typeList(["love","peace"])
typeList([5,7])

