class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrtoset = set(nums)

        if len(arrtoset) == len(nums):
            return False
        else:
            return True  