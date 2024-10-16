'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        for c in ransomNote:
            if c not in d:
                return False
            if d[c]<1:
                return False
            else:
                d[c]-=1
        return True
