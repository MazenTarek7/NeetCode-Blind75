class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        idx = 1
        for i in range(0 , len(nums) - 1):
            if (nums[i] == nums[idx]):
                return True
            else:
                idx += 1
        return False
