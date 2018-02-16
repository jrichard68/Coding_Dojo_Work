def odd_even():
    for count in range(1,2000):
        if count %2 != 0:
            print "Number is ", count, "This is an odd number."
        else:
            print "Number is ", count, "This is an even number."

odd_even()

'''Multiply: Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.'''

def multiply(my_list):
    new_list = [i * 5 for i in my_list]
    print(new_list)

multiply([2,4,10,16])

def layered_multiples(arr):
