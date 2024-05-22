from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pair = {}
        for index, num in enumerate(nums):
            if num in pair:
                return [pair[num], index]
            pair[target - num] = index


"""
TC = O(N)
SC = O(N)
"""