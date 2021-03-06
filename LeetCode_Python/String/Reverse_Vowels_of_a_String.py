'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution(object):
	def reverseVowels(self, s):
		VOWELS = {'a', 'e', 'i', 'o', 'u'}
		size = len(s)
		left, right = 0, size-1
		ls = list(s)
		while True:
			while left < size and s[left].lower() not in VOWELS:
				left += 1
			while right >= 0 and s[right].lower() not in VOWELS:
				right -= 1
			if left >= right:
				break
			ls[left], ls[right] = ls[right], ls[left]
			left, right = left + 1, right -1
		return ''.join(ls)
