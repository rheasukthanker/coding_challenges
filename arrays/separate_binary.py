'''
There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
'''
class Solution:
    def minimumSteps(self, s: str) -> int:
        white_position = 0
        total_swaps = 0

        # Iterate through each ball in the string
        for current_pos, char in enumerate(s):
            if char == "0":
                # Calculate the number of swaps needed
                total_swaps += current_pos - white_position

                # Move the next available position for a white ball one step to the right
                white_position += 1

        return total_swaps
