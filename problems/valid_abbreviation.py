class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                cur = 0
                while j < len(abbr) and abbr[j].isdigit():
                    if cur == 0 and abbr[j] == '0':
                        return False
                    cur = cur * 10 + int(abbr[j])
                    j += 1
                i += cur
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
