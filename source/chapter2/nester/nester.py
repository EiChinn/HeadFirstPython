movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", 'John Clease', 'Terry Gilliam', 'Eric Idle', 'Terry Johnes']]]

def print_lol(the_list, indent = False, level = 0):
    for sub_item in the_list:
        if isinstance(sub_item, list):
            print_lol(sub_item, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(sub_item)

print_lol(movies, True, level = 0)
