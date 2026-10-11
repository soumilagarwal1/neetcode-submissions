class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums = sorted(nums)

        for i, target in enumerate(nums):            
            end = len(nums)-1
            start = i + 1
            while start < end:
                if nums[start] + nums[end] > -target:
                    end -= 1
                elif nums[start] + nums[end] < -target:
                    start += 1
                else:
                    sol.add((nums[start], nums[end], target))
                    start += 1
                    end -= 1
            
        sol_fin = [list(t) for t in sol]

        return sol_fin

            





        