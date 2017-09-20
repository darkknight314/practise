# taking user input
n = int(input("Number of terms"))

# defining 3 var where c is the last var... i.e. sum of a and b
a = 1
b = 0
c = 1

# using a for to display the fib sequence
for i in range(1, n + 1):
    print(a)
    c = a + b
    b = a
    a = c

