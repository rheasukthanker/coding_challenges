'''You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.'''
'''Here, K is the last day we need to travel, the last value in the array days.

Time complexity: O(K).

The size of array dp is K+1, and we need to find the answer for each of the K states. For each state, the time required is O(1) as there would be only three recursive calls for each state. Therefore, the time complexity would equal O(K).

Space complexity: O(K).

The size of array dp is K+1; also, there would be some stack space required. The maximum active recursion depth would be K, i.e., one for each day. The size of the set isTravelNeeded will be equal to the size of days, i.e. N, considering the integers in days will always be strictly increasing we can say N<=K. Hence, the space complexity would equal O(K)'''
class Solution:
    def __init__(self):
        self.isTravelNeeded = set()
    
    def solve(self, dp, days, costs, currDay):
        # If we have iterated over travel days, return 0.
        if currDay > days[-1]:
            return 0
        
        # If we don't need to travel on this day, move on to next day.
        if currDay not in self.isTravelNeeded:
            return self.solve(dp, days, costs, currDay + 1)
        
        # If already calculated, return from here with the stored answer.
        if dp[currDay] != -1:
            return dp[currDay]
        
        oneDay = costs[0] + self.solve(dp, days, costs, currDay + 1)
        sevenDay = costs[1] + self.solve(dp, days, costs, currDay + 7)
        thirtyDay = costs[2] + self.solve(dp, days, costs, currDay + 30)
        
        # Store the cost with the minimum of the three options.
        dp[currDay] = min(oneDay, sevenDay, thirtyDay)
        return dp[currDay]
    
    def mincostTickets(self, days, costs):
        # The last day on which we need to travel.
        lastDay = days[-1]
        dp = [-1] * (lastDay + 1)
        
        # Mark the days on which we need to travel.
        self.isTravelNeeded = set(days)
        
        return self.solve(dp, days, costs, 1)
