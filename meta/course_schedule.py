'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.'''
'''### Time Complexity (TC):
- **Building the Graph:**
  - We iterate through the prerequisites list once to build the adjacency list. This takes **O(E)** time, where **E** is the number of prerequisites (edges).
- **DFS Traversal:**
  - Each course (node) is processed once, and each edge is traversed once. This results in a total time complexity of **O(V + E)**, where **V** is the number of courses (nodes) and **E** is the number of edges.

**Total Time Complexity:**  
O(V + E)

---

### Space Complexity (SC):
- **Graph Representation (Adjacency List):**
  - The adjacency list stores all edges, which requires **O(V + E)** space.
- **Visit Array:**
  - A visit array of size **V** is used to track the state of each node, contributing **O(V)** space.
- **Recursive Stack (DFS):**
  - In the worst case, the recursion stack can go up to **O(V)** deep if the graph forms a linear chain.

**Total Space Complexity:**  
O(V + E)

This is efficient and standard for graph traversal algorithms.'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        
        # Build the adjacency list
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
        
        visit = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        
        def dfs(node):
            if visit[node] == 1:  # Cycle detected
                return True
            if visit[node] == 2:  # Already checked and no cycle
                return False
            
            visit[node] = 1  # Mark as visiting
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            visit[node] = 2  # Mark as visited
            return False
        
        # Perform DFS on all courses
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
