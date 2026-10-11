class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        window = set()      # the characters currently inside s[start..end]
        maxl = 0

        for end in range(len(s)):
            # If s[end] is already in the window, shrink the window from the left
            # until that earlier copy has been removed.
            while s[end] in window:
                window.remove(s[start])
                start += 1

            # Now s[end] is safe to add: the window has no duplicates.
            window.add(s[end])

            # Record the window's size on every step, not only at duplicates.
            maxl = max(maxl, end - start + 1)

        return maxl