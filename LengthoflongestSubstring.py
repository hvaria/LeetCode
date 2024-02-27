class Solution:
	def lengthOfLongestSubstring(s):

		seen = {}
		left = 0
		output = 0

		for right in range(len(s)):
			if s[right] not in seen:
				output = max(output, right - left + 1)

			else:
				if seen[s[right]] < 1:
					output = max(output, right-left + 1)
				else:
					left = seen[s[right]] + 1

			seen[s[right]] = right
		return output

	s = 'oscddso'
	answer = lengthOfLongestSubstring(s)
	print(answer)