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
		hash = {}
		for i in range(len(nums)):
			if target - nums[i] in hash:
				return [hash[target-nums[i]], i]
			hash[nums[i]] = i
		return [-1, -1]

if __name__ == '__main__':
	result = Solution().twoSum([2, 7, 11, 15], 9)
	print result  #[0, 1]