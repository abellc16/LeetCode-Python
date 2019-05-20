# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        evens = []
        odds = []

        for item in A:
            if item % 2 == 0:
                evens.append(item)
            else:
                odds.append(item)

        for item in odds:
            evens.append(item)

        return evens


if __name__ == "__main__":
    print(Solution.sortArrayByParity(Solution, [3, 1, 2, 4]))
    print(Solution.sortArrayByParity(Solution, []))
    print(Solution.sortArrayByParity(Solution, [1]))
    print(Solution.sortArrayByParity(Solution, [2]))
    print(Solution.sortArrayByParity(Solution, [2, 4]))
    print(Solution.sortArrayByParity(Solution, [1, 11, 13]))
    print(Solution.sortArrayByParity(Solution, [5, 45, 20, 19, 99, 2135484]))
