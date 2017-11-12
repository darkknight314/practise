num_rows = int(input("number of rows"))

print(1)
for a in range(2,num_rows + 1):
    
    # k is a variable that is 1 less than the starting element of each row
    k = a*(a - 1)/2
    
    row = list(range(1 + int(k), int(k) + a + 1))
    
    # using a for loop directly in .join()
    print(" ".join(str(num) for num in row))
