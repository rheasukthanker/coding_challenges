'''There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int: 
        # Check if the total gas available is less than the total cost of traveling
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Initialize the net gas difference
        res = 0    # Initialize the starting index
        
        # Iterate through the gas stations
        for i in range(len(gas)):
            # Update the net gas difference
            total += (gas[i] - cost[i])
            
            # If the net gas difference becomes negative, reset to zero and update the starting index
            if total < 0:
                total = 0
                res = i + 1
        
        return res