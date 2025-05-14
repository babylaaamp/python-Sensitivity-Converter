#input origin game to convert sens to target game
from_game = input('Original Game > ')

#input sens of the origin gamae
from_sens = float(input('Enter Sens > '))

#input target game to convert sens to
to_game = input('Target Game > ')

#sens_converter function
def sens_converter(from_sens,from_game, to_game):
    #structure game
    games = {

        #example: val sens to cs2 sens is : valorant sens *3.18 = cs2 sens
        ('valorant','cs2'):3.18,
        ('valorant','csgo'):3.18,
        ('valorant','apex'):3.18,
        ('valorant','overwatch'):10.61,
        ('valorant','roblox'):5.74,
        ('valorant','marvel rivals'):4.0,
        ('valorant','rb6'):12.28
    }

    #key is to contain the value in sens_converter, if the game we input in dont match, will print error
    key = (from_game, to_game)
    if key not in games:
        print("Error, game is not in game list")
        return

    #factor is to use the number of multiply that we input the origin game and target game
    factor = games[key]

    #coverted is to store calculated sens
    converted = (from_sens*factor)

    #print out the calculated sens
    print(f"Converted sens > {converted:.3f}")

#use function
sens_converter(from_sens,from_game,to_game)