class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        curr_substr = dict()
        max_len = 0
        curr_len = 0

        while right < len(s):
            if (curr := s[right]) not in curr_substr:
                curr_substr[curr] = right
                right += 1
                curr_len = len(curr_substr)
                max_len = max(max_len, curr_len)
            else:
                new_left = curr_substr[curr] + 1
                for i in range(left, new_left):
                    del curr_substr[s[i]]
                left = new_left

                curr_substr[s[right]] = right
                right += 1

        return max_len
