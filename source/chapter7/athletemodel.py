import pickle
from athlete import Athlete

def get_coach_data(filename):
    try:
        with open(filename) as player_score:
            data = player_score.readline().strip().split(',')
            result = Athlete(data.pop(0), data.pop(0), data)
            return (result)
    except IOError as err:
        print('IOErroe: ' + str(err))
        return(None)
def put_to_store(file_list):
    all_athletes = {}
    for each_file in file_list:
        player = get_coach_data(each_file)
        all_athletes[player.name] = player
    try:
        with open('athletes.pickle', 'wb') as athletes:
            pickle.dump(all_athletes, athletes)
    except IOError as err:
        print('Error: ' + str(err))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athletes:
            all_athletes = pickle.load(all_athletes, athletes)
    except IOError as err:
        print('Error: ' + str(err))
    return(all_athletes)
            
