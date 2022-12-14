def attempt1():
    player_moves = []
    opponent_moves = []
    with open("input.txt", "r") as guide:
        lines = guide.readlines()
        for line in lines:
            moves = line.strip().split(" ")
            opponent_moves.append(moves[0])
            player_moves.append(moves[1])
            
    for move in range(len(lines)):
        print(opponent_moves[move], player_moves[move])

def attempt2():
    with open("input.txt") as f:
        guide = [[guide.split()[0], guide.split()[1]] for guide in f.readlines()]
        scores = {
            "A": 1,
            "B": 2,
            "C": 3
        }
        total_score = 0
        for opponent_choice, player_choice in guide:
            print(opponent_choice,player_choice)
            if opponent_choice == player_choice:
                round_score = 3
                print("DRAW")
            else:
                if (opponent_choice == "A" and player_choice == "C") or (opponent_choice == "B" and player_choice == "A") or (opponent_choice == "C" and player_choice == "B"):
                    round_score = 0
                    print("LOSS")
                else:
                    print("WIN")
                    round_score = 6
            total_score += round_score
        print(total_score)
attempt2()