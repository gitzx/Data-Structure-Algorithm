'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.
'''

'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
'''

class Solution(object):
	def Height(self, root):
		if root == None:
			return 0
		return max(self.Height(root.left), self.Height(root.right)) + 1
	def isBalanced(self, root):
		if root == None:
			return True
		if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
			return self.isBalanced(root.left) and self.isBalanced(root.right)
		else:
			return False

