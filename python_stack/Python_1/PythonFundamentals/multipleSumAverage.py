multiples part 1
for count in range(1,1000):
    print count

#multiples part  multiples of 5 from 5 to 1,000,000
count = 5
while count <= 1000000:
    print count
    count +=5

#Sum List-program that print sum of all values in list--after creating for loop to no avail found a built in function sum
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

# the below didn't work
'''a = [1, 2, 5, 10, 255, 3]
sum = 0
for count in range(0,len(a)):
  sum = sum + a[count], count
print sum''''
  
#Average List-program prints average of values in list
a = [1, 2, 5, 10, 255, 3]
b = sum(a) / float(len(a))
print b
  

