#movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", 'John Clease', 'Terry Gilliam', 'Eric Idle', 'Terry Johnes']]]

def print_lol(the_list):
    for sub_item in the_list:
        if isinstance(sub_item, list):
            print_lol(sub_item)
        else:
            print(sub_item)

#print_lol(movies)
