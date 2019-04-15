'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	Example:
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

class Solution(object):
  def twoSum(self, nums, target):
    mapping = {}
    
    for key,value in enumerate(nums):
      diff = target - value
      if diff in mapping:
        return [key, mapping[diff]]
      else:
        mapping[value] = key
      

# Space: O(N)
# Time: O(N)
