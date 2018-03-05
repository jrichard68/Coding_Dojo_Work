# declare a class and give it name User
class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed, miles):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        miles = 0
        self.miles = miles
    # this is a method we created to display the bike's price, maximum speed, and the total miles
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding" + (self.miles + 10)
        return self
    def reverse(self):
        print "Reverse" + (self.miles - 10)
        return self
#now create an instance of the class
bike1 = Bike("$100","25mph")
bike2 = Bike("$200","30mph")
bike3 = Bike("$300","30mph")
#print bike1.miles, bike2.miles, bike3.miles
