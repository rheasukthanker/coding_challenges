'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string '''
# TC: O(S), S is total number of chars in all strings In the worst case there will be n equal strings with length m and the algorithm performs S=m⋅n character comparisons.
#Even though the worst case is still the same as Approach 1, in the best case there are at most n⋅minLen comparisons where minLen is the length of the shortest string in the array.
# SC: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
