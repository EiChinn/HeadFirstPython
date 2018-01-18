import pickle

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role =='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
try:
    with open('man_data.txt', 'wb') as man_data, open('other_data.txt', 'wb') as other_data:
        pickle.dump(man, man_data)
        pickle.dump(other, other_data)
except IOError as err:
    print('File Error: ' + str(err))
except PickleError as perr:
    print('Pickling Error: ' + str(perr))

