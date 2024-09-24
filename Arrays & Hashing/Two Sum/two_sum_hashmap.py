"""
Time Complexity: O(n) - Single pass through the array.
Space Complexity: O(n).
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHashMap = {key: index for index, key in enumerate(nums)}
        ansArr = []
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if target - nums[i] in numsHashMap and numsHashMap[diff] != i:
                ansArr.append(i)
                ansArr.append(numsHashMap[diff])
                break
        return ansArr
