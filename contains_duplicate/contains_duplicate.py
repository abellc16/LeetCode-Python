# Author: Camby Abell
# Filename: contains_duplicate.py
# URL: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return False
        else:
            sorted_nums = sorted(nums)

            for i in range(0, len(sorted_nums) - 1):
                num1 = sorted_nums[i]
                num2 = sorted_nums[i + 1]

                if num1 == num2:
                    return True

        return False

if __name__ == "__main__":
    print(Solution.containsDuplicate(Solution, [1, 3, 2, 1]))
    print(Solution.containsDuplicate(Solution, [6, 3, 7, 9, 10, 10494]))
    print(Solution.containsDuplicate(Solution, [0]))