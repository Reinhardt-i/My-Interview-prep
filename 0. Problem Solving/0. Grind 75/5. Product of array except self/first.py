from functools import reduce
import operator

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)
        elif zeros == 1:
            product_non_zeros = reduce(operator.mul, (x for x in nums if x != 0), 1)
            return [product_non_zeros if x == 0 else 0 for x in nums]
        else:
            all_prod = reduce(operator.mul, nums, 1)
            return [all_prod // x for x in nums]
