"""
This code takes in input of lists and then returns the number of inversions
between elements required to sort the array. 

As it does not use recursive methods like mergesort, it is not very efficient
with large arrays

Input:
The first line contains an integer, , denoting the number of lists.
The  subsequent lines describe each list over two lines:
   1. The first line contains an integer, , denoting the number of elements 
      in the dataset.

   2. The second line contains  space-separated integers describing the 
      list.
 Output:
 1. Number of inversions required.

"""
d = int(input())
lists = []

for _ in range(d):
   length = int(input())

   input_list = list(map(int, input().split()))
   lists.append(input_list)


# this function uses nested loops to increment the variable "inversions"
# for each inversion performed.

def count_inversions(a):

   inversions = 0
   for i in range(0, len(a)):

      for j in range(i, len(a)):    # make more efficient

         # this is a really cool bit of python logic to invert two elements
         if a[i] > a[j]:

            a[i], a[j] = a[j], a[i]

            inversions += 1

         else:
            continue

   return(inversions)

for sequence in lists:
   print(count_inversions(sequence))
