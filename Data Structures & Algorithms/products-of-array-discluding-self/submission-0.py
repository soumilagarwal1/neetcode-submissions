class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        c = 0
        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                c += 1
        
        for num in nums:
            if c > 1:
                prod.append(0)
            elif c == 1:
                if num != 0:
                    prod.append(0)
                else:
                    prod.append(product)
            else:
                prod.append(product//num)
        
        return prod