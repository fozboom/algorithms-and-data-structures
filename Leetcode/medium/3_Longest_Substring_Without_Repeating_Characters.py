class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        curr_substr = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in curr_substr:
                curr_substr.remove(s[left])
                left += 1

            curr_substr.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len
