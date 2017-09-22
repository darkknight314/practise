i = int(input("number of rows"))

print(1)
for a in range(2, i + 1):
    k = a*(a - 1)/2
    bubu = list(range(1 + int(k), int(k) + a + 1))
    print(" ".join(str(m) for m in bubu))
