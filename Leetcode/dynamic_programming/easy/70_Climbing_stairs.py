class Solution(object):
    def climbStairs(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        steps = [None] * (n + 1)

        steps[1] = 1  # only 1 step
        steps[2] = 2  # 1 step + 1 step | 2 steps

        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n]
