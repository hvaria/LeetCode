class Solution:
	def longestPalindrome(s):

		s_rev = s[::-1]
		substring = ''
		max_substring = ''

		for letter in s:
			substring += letter

			while(substring not in s_rev):
				substring = substring[1:]

			else:
				if(substring == substring[::-1] and len(max_substring) < len(substring)):
					max_substring = substring

		return (max_substring)


	s = 'babad'
	answer = longestPalindrome(s)
	print(answer)