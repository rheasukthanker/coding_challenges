'''You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.'''
# TC O(n), SC O(n)
'''
The loop over order iterates , M times, where M is the length of the order string.For each character in order, popping from freq and multiplying takes 𝑂(1), O(1) on average. This results in a total time of 𝑂(𝑀). However we have only 26 chars so M is constant and overall TC is O(N)'''
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter
        freq = Counter(s)
        
        # Use list comprehension for efficiency
        result = [letter * freq.pop(letter) for letter in order if letter in freq]
        result.extend(letter * count for letter, count in freq.items())
        
        return ''.join(result)
