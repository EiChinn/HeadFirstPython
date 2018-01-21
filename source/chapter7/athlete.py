class Athlete(list):
    def __init__(self, name, dob = None, times = []):
        #The code to initialize an 'Athlete' objedt.
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)
        #print('self: ' + str(self))

    def sanitize(self, time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string
        (mins, secs) = time_string.split(splitter)
        return mins + '.' + secs

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self]))[0 : 3]

    
