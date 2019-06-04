# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/height-checker/


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        out_of_order = 0
        for i, j in zip(sorted_heights, heights):
            if i != j:
                out_of_order += 1

        return out_of_order


if __name__ == "__main__":
    print(Solution.heightChecker(Solution, [1,1,4,2,1,3]))
    print(Solution.heightChecker(Solution, [1,2,1,2,1,1,1,2,1]))