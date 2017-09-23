import random


i = random.randint(1000, 9999)
attempts = 1

print(" \t Bharre Gurre: The Guessing Game \n  ")
print(" \tInstructions \n")
print("For every digit that you guess correctly in the correct place, you have a 'bharre'.")
print("For every digit you guess correctly but in the wrong place, you get a 'gurre'.")
print("Every time the you make a guess, your number of attempts will be shown")
print("Once you guess the entire number correctly, the game is over. \n")


while True:
    try:
        print(" \t Bharre Gurre: The Guessing Game \n  ")

        print("Attempt Number: ", attempts)

        attempts += 1
        bharre = []
        gurre = []

        num = int(input("Please guess a four digit number \n Enter 0 to play another game \n"))
        a = list(str(num))
        b = list(str(i))

        if num == 0:
            break

        if len(a) < 4 or len(a) > 4:
            print("Please enter a four digit number")

        for x in a:
            if b[a.index(x)] == x:
                bharre.append(x)
                # print(bharre)

            elif x in b:
                gurre.append(x)
                # print(gurre)

        if len(bharre) == len(a):
            print("You got lucky")
            break

        print(str(len(bharre)) + "Bharre   " + str(len(gurre)) + "Gurre")
        print(" \n")

    except ValueError:
        print("Don't act like an idiot and enter a number")
        print(" \n")
