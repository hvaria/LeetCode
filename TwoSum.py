class Solution:
	def twoSum(nums, target):
		holder = {}
		for i in range(len(nums)):
			dif = target - nums[i]
			if dif in holder:
				return [holder[dif], i]

			holder[nums[i]] = i



	nums = [2,3, 7]
	target = 9

	answer = twoSum(nums, target)
	print(answer)