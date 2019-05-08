# Author: Camby Abell
# Filename: to_lower_case.py


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        # TRIVIAL SOLUTION
        return str.lower()


if __name__ == "__main__":
    print(Solution.toLowerCase(Solution, "UPPER"))
