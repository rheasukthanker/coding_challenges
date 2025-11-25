# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_counter = {}
        left = 0
        right = 0
        len_s = len(s)
        max_len = 0
        while right<len_s:
            if s[right] in char_counter:
                char_counter[s[right]]+=1
            else:
                char_counter[s[right]]=1
            while char_counter[s[right]]>1:
                char_counter[s[left]]=char_counter[s[left]]-1
                left = left+1
            max_len = max(max_len,right-left+1)
            right = right+1
        return max_len
               
