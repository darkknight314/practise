# this code moves the elements of an array to the left by k units
def array_left(a, n, k):

   for i in range(0, k):
      em = a[0]

      # removing an element from the start and then reinserting it at the back
      a.remove(em)
      a.append(em)

   return(a)

# taking input of the form:
# number of terms (space) number of moves to left(value of k)
# space separated array elements
n,k = map(int, input().split())
a = list(map(int, input().split()))
solution = array_left(a, n, k)

print(*solution, sep=' ')