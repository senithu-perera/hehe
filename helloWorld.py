import random

isPlayer_won = False
isCPU_won = False

while True:

    print("(S)isser - (R)ock - (P)apper")
    human_choice = input("Choose - ")

    human_choice_numarick = 0
    cpu_choice = 0
    player_choosen = False
    cpu_choosen = False

    

    if human_choice == "S":
        human_choice_numarick = 1
        player_choosen = True

    elif human_choice == "R":
        human_choice_numarick = 2
        player_choosen = True

    elif human_choice == "P":
        human_choice_numarick = 3
        player_choosen = True

    #cpu logic starts
    # Rock - 2 // Siscor - 1 // Paper - 3

    if player_choosen == True:
        cpu_choice = random.randint(1,4)

        if cpu_choice == 1:
            print("CPU choose - Sissors")
        if cpu_choice == 2:
            print("CPU choose - Rock")
        if cpu_choice == 3:
            print("CPU choose - Paper")

        player_choosen = False
        cpu_choosen = True

    if cpu_choosen == True:

        if human_choice_numarick == 1 and cpu_choice == 1:
            print("It's a tie")

        elif human_choice_numarick == 2 and cpu_choice == 2:
            print("It's a tie")

        elif human_choice_numarick == 3 and cpu_choice == 3:
            print("It's a tie")

        elif human_choice_numarick == 1 and cpu_choice == 2:
            print("CPU wins!!")
            isCPU_won = True

        elif human_choice_numarick == 1 and cpu_choice == 3:
            print("You win!!")
            isPlayer_won = True

        elif human_choice_numarick == 2 and cpu_choice == 1:
            print("You win!!")
            isPlayer_won = True

        elif human_choice_numarick == 2 and cpu_choice == 3:
            print("CPU wins!!")
            isCPU_won = True

        elif human_choice_numarick == 3 and cpu_choice == 1:
            print("CPU wins!!")
            isCPU_won = True

        elif human_choice_numarick == 3 and cpu_choice == 2:
            print("You win!!")
            isPlayer_won = True

    cpu_choosen = False

