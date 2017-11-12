# user input for number of years
years = int(input())

# recursive function(similarity to fibonacci sequence: fib seq x 2)
def drag_num(n):
   if n < 2:
      return(2)

   elif n >= 2:
      return(drag_num(n - 1) + drag_num(n - 2))

# printing out result
solution = drag_num(years)
print(solution)


   