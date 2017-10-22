import random

path = 'C:\\Users\sangeeta karajgi\Downloads\hangman.txt'

hangman = open(path, 'r')
thewords = hangman.readlines()
used = []

word = thewords[random.randrange(1, 267751, 1)]

dis = ["__"] * (len(word) - 1)

print(" ".join(dis))

p = 1
while "__" in dis:
    print("Attempt number: ", p)
    usr = input("guess(in caps) \t")

    p += 1

    if usr in used:
        print("already guessed")
        print(" \n")
        continue

    elif len(usr) > 1:
        print("only one letter")
        print(" \n")
        continue

    try:
        check = int(usr)
        print("idiot")
        print(" \n")
        continue

    except ValueError:
        pass

    used.append(usr)

    for idx, lets in enumerate(word):

        if lets == usr:
            dis[idx] = usr

    print(" ".join(dis))
    print(" \n")
