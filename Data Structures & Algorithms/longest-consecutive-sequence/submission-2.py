class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        nummap = {}

        for num in nums:
            nummap[num] = 1

        for key, value in nummap.items():
            keycopy = key
            c = 1
            while nummap.get(keycopy+c, 0) != 0:
                nummap[keycopy] += nummap[keycopy+c]
                nummap[keycopy+c] = 0
                c += 1
        
        if len(nums) != 0:
            return max(nummap.values())
        
        else:
            return 0
            


        