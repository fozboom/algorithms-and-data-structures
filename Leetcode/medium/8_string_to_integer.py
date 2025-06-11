class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        s = s.lstrip()
        if not s:
            return 0

        result = 0
        base_power = 0

        i = 0
        sign = 1
        if s[i] == '-' or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            base_power += 1

            i += 1

            if sign * result > MAX_INT:
                return MAX_INT
            if sign * result < MIN_INT:
                return MIN_INT

        result *= sign
        return result


def test():
    s = Solution()
    assert s.myAtoi('123') == 123
    assert s.myAtoi('1337c0d3') == 1337
    assert s.myAtoi('-123k8') == -123

    assert s.myAtoi(' -042') == -42
    assert s.myAtoi('words and 987') == 0
    assert s.myAtoi('-91283472332') == -2147483648
    assert s.myAtoi('2147483648') == 2147483647

    print('Tests passed')


test()
