class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nummap = {}
        for num in nums:
            nummap[num] = nummap.get(num, 0) + 1
        numdict = dict(sorted(nummap.items(), key=lambda item: item[1], reverse=True))

        output = []
        c = 0
        for key, value in numdict.items():
            if c == k:
                return output
            
            output.append(key)
            c += 1
        
        return output


        
            




