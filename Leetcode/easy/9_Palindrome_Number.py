class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = 0

        n = x

        while n > 0:
            result = result * 10 + n % 10
            n //= 10

        return result == x


s = Solution()

assert s.isPalindrome(121)
assert not s.isPalindrome(12343)
assert not s.isPalindrome(-121)

assert s.isPalindrome(123454321)
assert s.isPalindrome(0)
