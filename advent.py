with open("adventinput.txt") as f:
    data = f.readlines()

#take care of newline character
game_dict = {
        "A" : ["rock" , 1] , "B": ["paper" , 2] , 
        "C" : ["scissor" , 3],"X" : ["lose" , 1] , 
        "Y": ["draw" , 2] , "Z" : ["win" , 3]
        }

total = 0
for line in data:
    line = line.replace("\n" , "")
    first_player = game_dict[line[0]]
    second_player = game_dict[line[2]]

    if first_player[0] == "rock":
        if second_player[0] == "lose":
            total += 3 
        elif second_player[0] == "draw":
            total += first_player[1] + 3
        else:
            total += 6 + 2

    elif first_player[0] == "paper":
        if second_player[0] == "lose":
            total += 0 + 1
        elif second_player[0] == "draw":
            total += first_player[1] + 3
        else:
            total += 6 + 3

    else:
        if second_player[0] == "lose":
            total += 0 + 2
        elif second_player[0] == "draw":
            total += first_player[1] + 3
        else:
            total += 6 + 1


print(total)


