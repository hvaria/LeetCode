class Solution:
	def findMedianSortedArrays(nums1, nums2):
		
		if len(nums1) < len(nums2):
			a, b = nums1, nums2
		else:
			a, b = nums2, nums1

		left, right, half = 0, len(a) - 1, (len(a) + len(b)) // 2

		while True:
			i = (left + right) // 2
			j = half - i - 2

			a_current = a[i] if i >= 0 else float('-inf')
			a_right = a[i + 1] if i + 1 < len(a) else float('inf')
			b_current = b[j] if j >= 0 else float('-inf')
			b_right = b[j + 1] if j + 1 < len(b) else float('inf')

			if a_current <= b_right and b_current <= a_right:
				if(len(a) + len(b)) % 2:
					return min(a_right, b_right)
				else:
					return (max(a_current, b_current) + min(a_right, b_right)) / 2
			elif a_current > b_right:
				right =i - 1
			else: 
				left = i+1 

	nums2 = [2]
	nums1 = [1,3,7, 0]
	answer = findMedianSortedArrays(nums1, nums2)
	print(answer)