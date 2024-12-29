'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.'''
# TC: O(max(m,n)), SC: O(1)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        s = ""
        i = 0
        j = 0
        while i<len_w1 or j<len_w2:
            if i<len_w1:
                s=s+word1[i]
                i = i+1
            if j<len_w2:
                s=s+word2[j]
                j = j+1
        return s
