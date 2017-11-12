num_staircases = int(input())
staircase_heights = []

for i in range(num_staircases):
   height = int(input())
   staircase_heights.append(height)


def ways(steps, mem = {0: 0, 1: 1}):
   if steps not in mem:
      mem[steps] = ways(steps, mem)  

      if steps >= 0:

         if steps == 1:
            return(1)

         elif steps == 0:
            return(1)                        # check commented part

         elif steps == 2:
            return(mem[steps - 1] + mem[steps - 2])

         elif steps >= 3:
            return(mem[steps - 1] + mem[steps - 2] + mem[steps - 3])

   else:
      pass


for height in staircase_heights:
   solution = ways(height)
   print(solution)


"""d = 0
      for j in range(3):
         d += ways(steps - j)             ####

      return(d)"""