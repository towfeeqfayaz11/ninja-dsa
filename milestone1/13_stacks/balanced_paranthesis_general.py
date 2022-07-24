# if the string contains any of the paranthesis -> (, {, [
# NOTE: Brackets are said to be balanced if the bracket which opens last, closes first.

from sys import stdin


def isBalanced(expression) :
	stack = []
	for c in expression:
		if c in "({[":                               # if char is any opening paranthesis -> (,{,[
			stack.append(c)
		elif c == ")":                               # if char is closing paranthesis -> )
			if (not stack) or stack[-1] != "(":      # if stack is empty return false or if last element of staxk is not (, then also return false
				return False
			stack.pop()
		elif c == "}":
			if (not stack) or stack[-1] != "{":
				return False
			stack.pop()
		elif c == "]":
			if (not stack) or stack[-1] != "[":
				return False
			stack.pop()
	
	if (not stack):
		return True
	else:
		return False



#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")
else :
	print("false")