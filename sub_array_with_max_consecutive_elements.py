"""
This code basically takes a list, tries swapping certain elements based on certain conditions and returns the max possible sub-array that can be formed consisting of
the same element.
--------------------
Details:
1.The list contains only binary elements(0's and 1's).
2.The number of inversions(by user input) is the max number of "swaps" between 
 0 and 1 to form the max possible sub-array with same elements.
-------------------- 
Input:
1.Comma separated list elements(should be only 1's and 0's)(var_name = sequence)
2. number of inversions(var_name = inversions)
--------------------
Output:
1.Longest possible sub-arrays consisting of same elements. 
	They can be more than 1 as the sub_array elements can be 0's or 1's.
---------------------
Sample 1:
input: 0 0 0
	   3
	   
output: [0, 0, 0]
		[1, 1, 1]   
Explanation: since at max 3 elements can be swapped.
---------------------
Sample 2:
input: 0 0 0
	   2
	   
output: [0, 0, 0] 

Explanation: since at max 2 elements can be swapped. But, the original sequence
already has 3 consecutive 0's which is more than [1, 1]
---------------------
Key concepts:
1. random library to choose different indexes of the list
2. list variables cannot be directly copied.. as they create a reference to the
	original list. List splicing must be used.
3. Using enumerate() and zip() to iterate over multiple lists at the same time.
	(zip was used in trial but later removed as enumerate performed the same 
	function)
"""

import random

sequence = list(map(int, input().split()))
inversions = int(input())

sub_arrays_0_1 = []
sub_arrays = []

lengths = []

# ********************************************

def inversion_trial_0_1(sub_array):

	sub_array_trial = sub_array[:]
	
	zeros = []
	ones = []
	
	for ele_id, ele in enumerate(sub_array):
		if ele == 0:
	
			zeros.append(ele_id)
	

	for l in range(0, inversions + 1):
		if l <= len(zeros):
			inversion_possi = random.sample(zeros, l)

			for i in inversion_possi:
				sub_array_trial[i] = 1

			if 0 not in sub_array_trial:

				if sub_arrays_0_1.count(sub_array_trial) == 0:
					sub_arrays_0_1.append(sub_array_trial)

# *****************************************

def inversion_trial_1_0(sub_array):

	sub_array_trial = sub_array[:]
	
	zeros = []
	ones = []
								
	for ele_id, ele in enumerate(sub_array):
		if ele == 1:
	
			ones.append(ele_id)

	for l in range(0, inversions + 1):
		if l <= len(ones):
			inversion_possi = random.sample(ones, l)

			for i in inversion_possi:
				sub_array_trial[i] = 0

			if 1 not in sub_array_trial:

				if sub_arrays_0_1.count(sub_array_trial) == 0:
					sub_arrays_0_1.append(sub_array_trial)
			
# *********************************************

def return_sub_arrays(input_list):
	
	for i in range(0, len(input_list)):
	
		for k in range(i, len(input_list)):
			
			sub_array = input_list[i:k + 1]
			
			if sub_arrays.count(sub_array) == 0:
				sub_arrays.append(sub_array)
		
		for sub_array in sub_arrays:			
			
				inversion_trial_0_1(sub_array)
				inversion_trial_1_0(sub_array)
		

return_sub_arrays(sequence)

# ********************************************

def return_max_len_sub_array(input_list):
	for i in input_list:
		lengths.append(len(i))
	
	max_sub_array = max(lengths)
	
	for length_id, length in enumerate(lengths):
		if length == max_sub_array:
			print(sub_arrays_0_1[length_id])
	
return_max_len_sub_array(sub_arrays_0_1)

# *********************************************


