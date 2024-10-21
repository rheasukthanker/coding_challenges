'''Given a string s, find the length of the longest substringwithout repeating characters.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        last_index = {}
        
        start = 0
        for end in range(n):
            current_char = s[end]
            start = max(start, last_index.get(current_char, 0))
            max_length = max(max_length, end - start + 1)
            last_index[current_char] = end + 1
        
        return max_length
            
