class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        fib = [None] * (n + 1)

        fib[0] = 0
        fib[1] = fib[2] = 1

        for i in range(3, n + 1):
            fib[i] = fib[i - 3] + fib[i - 2] + fib[i - 1]

        return fib[n]
