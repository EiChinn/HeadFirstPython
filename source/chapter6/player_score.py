from Athlete import Athlete


def get_player_data(filename):
    try:
        with open(filename) as player_score:
            data = player_score.readline().strip().split(',')
            result = Athlete(data.pop(0), data.pop(0), data)
            return (result)
    except IOError as err:
        print('IOErroe: ' + str(err))
        return(None)

sarah = get_player_data('./score/sarah2.txt')
sarah.append('0.25')
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
        
james = get_player_data('./score/james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))

julie = get_player_data('./score/julie2.txt')
print(julie.name + "'s fastest times are: " + str(julie.top3()))

mikey = get_player_data('./score/mikey2.txt')
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
