# initially:
game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

a = 1

while a <= 9:
    print(" \t TIC-TAC-TO \n")
    print("current state:")
    print("  ".join(str(a) for a in game[0]))
    print("  ".join(str(a) for a in game[1]))
    print("  ".join(str(a) for a in game[2]))

    turn = list((input(" play your move as: \nrow column letter \n")).split(" "))
    i = int(turn[0])
    j = int(turn[1])

    while True:

        try:
            if game[i - 1][j - 1] == 0:
                game[i - 1][j - 1] = turn[2]
                break

            else:
                print("Space occupied")
                break
        except ValueError:
            print(" only x and o")
            print(" \n")

    a += 1

    # to count the number of x's and o's...
    xs = 0
    os = 0
    for i in range(0, 3):
        xs += game[i].count("x")
        os += game[i].count("o")

    # winning conditions:

    # i presume you understood xs and os == 3..
    # the 5 is because of a special case when a L or X shaped design is made..
    # try it out

    if xs == 3 or xs == 5 or os == 3 or os == 5:
        # horizontal check:
        if len(set(game[0])) == 1:
            if "o" in set(game[0]):
                print("o wins")
                break
            elif "x" in set(game[0]):
                print("x wins")
                break

        elif len(set(game[1])) == 1:
            if "o" in set(game[1]):
                print("o wins")
                break

            elif "x" in set(game[1]):
                print("x wins")
                break

        elif len(set(game[2])) == 1:
            if "o" in set(game[2]):
                print("o wins")
                break

            elif "x" in set(game[2]):
                print("x wins")
                break

        # vertical check:
        elif game[0][0] == game[1][0] == game[2][0] == "o":
            print("o wins")
            break

        elif game[0][0] == game[1][0] == game[2][0] == "x":
            print("x wins")
            break

        elif game[0][1] == game[1][1] == game[2][1] == "o":
            print("o wins")
            break

        elif game[0][1] == game[1][1] == game[2][1] == "x":
            print("x wins")
            break

        elif game[0][2] == game[1][2] == game[2][2] == "o":
            print("o wins")
            break

        elif game[0][2] == game[1][2] == game[2][2] == "x":
            print("x wins")
            break

        elif game[0][0] == game[1][0] == game[2][0] == "o":
            print("o wins")
            break

        # diagonal check:
        elif game[0][0] == game[1][1] == game[2][2] == "o":
            print("o wins")
            break

        elif game[0][2] == game[1][1] == game[2][0] == "o":
            print("o wins")
            break

        elif game[0][0] == game[1][1] == game[2][2] == "x":
            print("x wins")
            break

        elif game[0][2] == game[1][1] == game[2][0] == "x":
            print("x wins")
            break

    else:
        print("no winner yet")
        print(" \n")

# for draw case:
if a == 10:
    print("draw")
