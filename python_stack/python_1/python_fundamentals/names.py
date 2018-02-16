#Part 1: write a function given the following list that creates outputs of:
#Michael Jordan
#John Rosales
#Mark Guillen
#KB Tonel'''

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names(arr):
   for student in students:
    print student['first_name'], student ['last_name']

print_names(students)

#Part 2-Create a program that prints the following format (including number of characters in each combined name):

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def print_users(dict):
    for key in users:
        print key
        our_list = users[key]
        for idx, person in enumerate(users[key]):
            print "{} - {} {} - {}".format(idx + 1, person['first_name'], person['last_name'], len(person['first_name'] + person['last_name']))

print_users(users)