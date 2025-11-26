# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping and stack:
                top_elem = stack.pop()
                if top_elem!=mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack 