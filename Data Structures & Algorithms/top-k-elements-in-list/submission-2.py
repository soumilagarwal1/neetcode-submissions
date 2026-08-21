class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nummap = {}
        for num in nums:
            if num not in nummap:
                nummap[num] = 1
            else:
                nummap[num] += 1
        nummap = dict(sorted(nummap.items(), key = lambda item: item[1], reverse = True))

        output = []
        for key, value in nummap.items():
            if k > 0:
                output.append(key)
                k -= 1
        
        return output


