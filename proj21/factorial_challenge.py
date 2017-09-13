# using a function to determine factorial
def fact():
    d = 1
    y = int(input("Please enter the number for which you want the factorial"))

    # using for loop to multiply previous values to d
    for i in range(1, y + 1):
        d *= i
    print(d)
fact()
