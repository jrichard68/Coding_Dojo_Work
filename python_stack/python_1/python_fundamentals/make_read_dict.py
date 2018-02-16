#Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.  Write a function that will print something like the following as it executes:

def print_dict(about_me):
    print "My name is", about_me["Name"]
    print "I am", about_me["Age"],"years old"
    print "My country of birth is", about_me["Country of Birth"]
    print "My favorite language is", about_me["Favorite Language"]


about_me = {
    "Name": "Jamie",
    "Age": 50,
    "Country of Birth": "The United States",
    "Favorite Language": "Python"
}
#print about_me["Name"]
print_dict(about_me)