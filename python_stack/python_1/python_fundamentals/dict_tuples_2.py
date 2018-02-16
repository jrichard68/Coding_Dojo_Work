def dictionary_tuples(any_dictionary):
    print [tuple(reversed(x)) for x in any_dictionary.items()]
# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dictionary_tuples(my_dict)