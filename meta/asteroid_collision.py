'''We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.'''
# TC: O(n) SC: O(n)
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

