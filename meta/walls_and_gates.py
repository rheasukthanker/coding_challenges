'''You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.'''
# TC: O(mn), SC O(mn)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                # negative asteroid destroys others in stack one by one
                while len(stack) > 0 and stack[-1] < abs(x):
                    stack.pop()
                # negative asteroid destroyed everyone
                if len(stack) == 0:
                    ans.append(x)
                # negative asteroid was beaten by positive asteroid (stack[-1])
                else:
                    # they destroyed each other
                    if stack[-1] == abs(x):
                        stack.pop()
        ans += stack
        return ans
