class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		matchingMap = {"}": "{", ")": "(", "]": "["}
		for c in s:
			if c in matchingMap: # Get closing parentheses
				if stack and stack[-1] == matchingMap[c]:
					stack.pop()
				else:
					return False
			else:
				stack.append(c)
				
		return True if not stack else False