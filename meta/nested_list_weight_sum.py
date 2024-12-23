'''You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#DFS
# Let N be the total number of nested elements in the input list
'''Time complexity : O(N).

Recursive functions can be a bit tricky to analyze, particularly when their implementation includes a loop. A good strategy is to start by determining how many times the recursive function is called, and then how many times the loop will iterate across all calls to the recursive function.

The recursive function, dfs(...) is called exactly once for each nested list. As N also includes nested integers, we know that the number of recursive calls has to be less than N.

On each nested list, it iterates over all of the nested elements directly inside that list (in other words, not nested further). As each nested element can only be directly inside one list, we know that there must only be one loop iteration for each nested element. This is a total of N loop iterations.

So combined, we are performing at most 2⋅N recursive calls and loop iterations. We drop the 2 as it is a constant, leaving us with time complexity O(N).

Space complexity : O(N).

In terms of space, at most O(D) recursive calls are placed on the stack, where D is the maximum level of nesting in the input. For example, D=2 for the input [[1,1],2,[1,1]], and D=3 for the input [1,[4,[6]]].

In the worst case, D=N, (e.g. the list [[[[[[]]]]]]) so the worst-case space complexity is O(N).'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total

        return dfs(nestedList, 1)

#BFS
'''Time complexity : O(N).

Similar to the DFS approach. Each nested element is put on the queue and removed from the queue exactly once.

Space complexity : O(N).

The worst-case for space complexity in BFS occurs where most of the elements are in a single layer, for example, a flat list such as [1, 2, 3, 4, 5] as all of the elements must be put on the queue at the same time. Therefore, this approach also has a worst-case space complexity of O(N).'''

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)

        depth = 1
        total = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                nested = queue.pop()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extendleft(nested.getList())
            depth += 1

        return total
