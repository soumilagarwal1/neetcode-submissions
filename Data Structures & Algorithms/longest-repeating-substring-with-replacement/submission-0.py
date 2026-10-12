class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = {}
        maxl = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            while (i - start + 1) - max(freq.values()) > k:
                freq[s[start]] -= 1
                start += 1
            maxl = max(maxl, i - start + 1)

        return maxl




                
            

        