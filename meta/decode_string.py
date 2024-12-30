'''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.'''
# TC: O(len_str*max(repeats)) SC: O(m+n)
'''Time Complexity: O(maxK⋅n), where maxK is the maximum value of k and n is the length of a given string s. We traverse a string of size n and iterate k times to decode each pattern of form k[string]. This gives us worst case time complexity as O(maxK⋅n).

Space Complexity: O(m+n), where m is the number of letters(a-z) and n is the number of digits(0-9) in string s. In worst case, the maximum size of stringStack and countStack could be m and n respectively.

'''
class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currentString = ""
        k = 0

        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                countStack.append(k)
                stringStack.append(currentString)
                currentString = ""
                k = 0
            elif ch == ']':
                decodedString = stringStack.pop()
                currentK = countStack.pop()
                currentString = decodedString + currentString * currentK
            else:
                currentString += ch

        return currentString
