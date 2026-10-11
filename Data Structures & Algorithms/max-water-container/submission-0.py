class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nummap = {}
        start = 0
        end = len(heights) - 1
        max = 0
        while start < end:
            area = min(heights[start], heights[end])*(end - start)
            if area > max:
                max = area
            if min(heights[start], heights[end]) == heights[start]:
                start += 1
            else:
                end -= 1
        
        return max
            
        