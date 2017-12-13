"""
Marc loves cupcakes, but he also likes to stay fit. He eats  cupcakes in one sitting, and each cupcake  has a calorie count, c. After eating a cupcake with c calories, he must walk at least c*2**j (where j is the number cupcakes he has already eaten) miles to maintain his weight.

Given the individual calorie counts for each of the total cupcakes, find and print a integer denoting the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.

Input:
1st line: total number of cupcakes
2nd line: space-separated calorie values of each cupcake

Output:
single value of the minimum distance travelled

Sample:
Input:
3(var: cupcakes)
1 3 2(var: calories)

Output:
11(var: distance)

Explanation: 3*2**0 + 2*2**1 + 1*2**2 = 11

Logic:
The cupcakes should be eaten in decreasing order of calorie content
"""


cup_cakes = int(input())

calories = list(map(int, input().split()))
calories_sorted = sorted(calories)

distance = 0
for cal_id, cal in enumerate(calories_sorted):
	distance += cal * 2 ** (len(calories_sorted) - 1 - cal_id)


print(distance)
	
