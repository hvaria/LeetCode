class Solution:
	def isPalindrome(x):
		if x<0:
			return False
		return str(x) == str(x)[::-1]

	x =121
	y = -212
	x_answer = isPalindrome(x)
	y_answer = isPalindrome(y)
	print(x_answer, y_answer)
