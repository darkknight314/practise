# printing pascal's Triangle.. taking input
i = int(input("Number of Rows"))

# using factorial function defined in another challenge


def fact(x):
    d = 1

    # using for loop to multiply previous values to d

    for j in range(1, x + 1):
        d *= j
    return d

# using nested for loops...  ,end=""  is used to continue on same line after ""..


for a in range(0, i + 1):
    print(" " * (i + 1 - a), end="")
    for p in range(0, a + 1):

        print(int(fact(a) / (fact(a-p)*fact(p))), end=" ")

    print(" \n")
