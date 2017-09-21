x = []
for i in range(1000, 3001):
    # separating the digits of i
    a = list(str(i))

    for b in a:
        if int(b) % 2 == 0:
            x.append(b)

        # verifying if all digits are even
    if len(x) == len(a):
        print("".join(x))
    else:
        x = []



