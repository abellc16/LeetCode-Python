# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/height-checker/

# NOT SOLVED AS OF 6/3/2019 #

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        out_of_order = 0
        for i in range(0, len(heights) - 1):
            j = heights[i + 1]
            if heights[i] > heights[j]:
                out_of_order += 1

        return out_of_order

if __name__ == "__main__":
    print(Solution.heightChecker(Solution, [1,1,4,2,1,3]))