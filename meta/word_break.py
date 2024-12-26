'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.'''
'''Given n as the length of s, m as the length of wordDict, and k as the average length of the words in wordDict,

Time complexity: O(n⋅m⋅k)

There are n states of dp(i). Because of memoization, we only calculate each state once. To calculate a state, we iterate over m words, and for each word perform some substring operations which costs O(k). Therefore, calculating a state costs O(m⋅k), and we need to calculate O(n) states.

Space complexity: O(n)

The data structure we use for memoization and the recursion call stack can use up to O(n) space.'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #This decorator @cache is used to memoize the results of the function(i).
        #Memoization ensures that results for the same input are stored and reused, avoiding redundant calculations and improving performance.
        @cache
        def dp(i):
            # if i is negative we have processed the full string
            if i < 0:
                return True

            for word in wordDict:
                # check if word, len(word) before i matches word, and check if remaining, ie word upto i-len(word)+1 matches word
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True # if yes, we can segment and return true

            return False # segmentation not possible, return false

        return dp(len(s) - 1) # check for len(s)
#DFS 
'''Given n as the length of s, m as the length of wordDict, and k as the average length of the words in wordDict,

Time complexity: O(n**3+m⋅k)

There are O(n) nodes. Because of seen, we never visit a node more than once. At each node, we iterate over the nodes in front of the current node, of which there are O(n). For each node end, we create a substring, which also costs O(n).

Therefore, handling a node costs O(n**2), so the BFS could cost up to O(n**3). Finally, we also spent O(m⋅k) to create the set words.

Space complexity: O(n+m⋅k)

We use O(n) space for queue and seen. We use O(m⋅k) space for the set words.'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False
