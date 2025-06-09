class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        max_dev = 1
        
        res_sign = -1 if x < 0 else 1
        x = abs(x)
        while x / max_dev >= 10:
            max_dev *= 10

        res = 0
        while x > 0:
            last_num = x % 10
            x = x // 10
            res += last_num * max_dev
            max_dev //= 10

        res *= res_sign
        if res < -(2**31) or res > (2**31 - 1):
            res = 0

        return res



def test():
    sol = Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(0) == 0
    assert sol.reverse(1534236469) == 0

test()