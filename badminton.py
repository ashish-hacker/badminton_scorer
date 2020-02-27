


player1 = input('Player One : ')
player2 = input('Player Two : ')

p1_points = [0, 0, 0, 0]
p2_points = [0, 0, 0, 0]
#The fourth slot stores the number of sets won by that player

current = 0




def display_score(p1_points, p2_points):

    print('-----------------------------------------')
    print( f"{player1}\t" +  "|" +str(p1_points[0]) + "\t" + "|" +str(p1_points[1]) + "\t" + "|" + str(p1_points[2]) + "\t" + "|")
    print('-----------------------------------------')
    print( f"{player2}\t" +  "|" +str(p2_points[0]) + "\t" + "|" +str(p2_points[1]) + "\t" + "|" + str(p2_points[2]) + "\t" + "|")
    print('-----------------------------------------')


def match_finished(player):
    pass


def start_match():

    current_set = 1
    match_not_finished = True

    while match_not_finished:

        current = int(input('[1/2] ==>'))
        if current == 1:
            p1_points[current_set-1] += 1
        else:
            p2_points[current_set-1] += 1

        if p1_points[current_set-1] == 11:
            p1_points[3] += 1
            current_set += 1
        elif p2_points[current_set-1] == 11:
            p2_points[3] += 1
            current_set += 1

        display_score(p1_points, p2_points)

        if p1_points[3] == 2:
            match_not_finished = False
            match_finished(1)
        elif p2_points[3] == 2:
            match_not_finished = False
            match_finished(2)
