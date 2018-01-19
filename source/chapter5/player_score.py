
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs
def get_player_data(filename):
    try:
        with open(filename) as player_score:
            result = player_score.readline()
            return (result.strip().split(','))
    except IOError as err:
        print('IOErroe: ' + str(err))
        return(None)
james = []
sarah = []
julie = []
mikey = []


james = get_player_data('./score/james.txt')
sarah = get_player_data('./score/sarah.txt')
julie = get_player_data('./score/julie.txt')
mikey = get_player_data('./score/mikey.txt')

james = [sanitize(time_string) for time_string in james]
sarah = [sanitize(time_string) for time_string in sarah]
julie = [sanitize(time_string) for time_string in julie]
mikey = [sanitize(time_string) for time_string in mikey]

unique_james = sorted(set(james))[0 : 3]
print(unique_james)

unique_sarah = sorted(set(sarah))[0 : 3]
print(unique_sarah)

unique_julie = sorted(set(julie))[0 : 3]
print(unique_julie)

unique_mikey = sorted(set(mikey))[0 : 3]
print(unique_mikey)

        
