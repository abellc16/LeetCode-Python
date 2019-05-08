# Author: Camby Abell
# Filename: judge_circle.py


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        norm = moves.upper()
        x = 0
        y = 0

        if len(norm) == 0:
            return True
        else:
            for i in norm:
                if i == "U":
                    y += 1
                elif i == "D":
                    y -= 1
                elif i == "R":
                    x += 1
                elif i == "L":
                    x -= 1

        if x == 0 and y == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution.judgeCircle(Solution, "lud"))

