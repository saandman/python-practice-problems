"""
Given a distinct array of numbers, and a target sum, return a sub-list of two numbers from that array that produce that sum.
"""

# O(n) time | O(n) space
def twoNumberSum(array, targetsum):
	num_hash = {}
	for num in array:
		potential_match = targetsum - num
		if potential_match in num_hash:
			# return [potential_match, num]
			print([potential_match, num])
			continue
		else:
			num_hash[num] = True
	if len(num_hash) == 0:
		return []

array = [1,2,3,7,8,5,-3,-5,-2,-6]
targetsum = 10

print(twoNumberSum(array, targetsum))