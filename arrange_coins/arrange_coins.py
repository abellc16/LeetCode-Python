# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/arranging-coins/


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        num_stairs = 0
        stair = 1
        coins = n

        if n == 1:
            return 1
        else:
            while coins >= stair:
                num_stairs += 1
                coins = coins - stair
                stair += 1

        return num_stairs

if __name__ == "__main__":
    print(Solution.arrangeCoins(Solution, 8))  # Expected: 3
    print(Solution.arrangeCoins(Solution, 5))  # Expected: 2