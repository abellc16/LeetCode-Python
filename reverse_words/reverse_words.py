# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_list = s.split()
        answer = ""

        for i in range(0, len(new_list)):
            new_list[i] = new_list[i][::-1]

        for item in new_list:
            answer = answer + str(item) + " "

        return answer.strip()


if __name__ == "__main__":
    print(Solution.reverseWords(Solution, "Let's take LeetCode contest"))