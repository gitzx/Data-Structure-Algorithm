'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
	def divide(self, dividend, divisor):
		INT_MAX = 2147483647
		if divisor == 0:
			return INT_MAX
		a, b = abs(dividend), abs(divisor)
		ans, shift = 0, 31
		while shift >= 0:
			if a >= b << shift:
				a -= b << shift
				ans += 1 << shift
			shift -= 1
		if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
			ans = - ans 
		if ans > INT_MAX:
			return INT_MAX
		return ans
		