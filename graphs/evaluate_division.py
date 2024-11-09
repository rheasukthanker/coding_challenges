'''You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them. O(m+n)

'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a/b = 2; b/a = 1/2
        b/c = 3; c/b = 1/3
        a/c = a/b * b/c = 2 * 3 = 6
        """
        # Construct graph
		# Reciprocal value enables bidirectional access
        n = len(equations)
        graph = defaultdict(dict)
        for idx, (src, dest) in enumerate(equations):
            graph[src][dest] = values[idx]
            graph[dest][src] = 1/values[idx]
        
        # DFS to process the result of queries
        def dfs(src, dest, res):
            if src not in graph or dest not in graph or src in visited:
                return -1
            if src == dest:
                return res
            visited.add(src)
            for nei, val in graph[src].items():
                temp = dfs(nei, dest, res * val)
                if temp != -1:
                    return temp
            return -1
        
        # Traverse over the queries and store the processed queries in result list
        result = []
        for src, dest in queries:
            visited = set()
            val = dfs(src, dest, 1)
            result.append(val)
            
        return result
