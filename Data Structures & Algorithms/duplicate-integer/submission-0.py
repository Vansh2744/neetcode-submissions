class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        not_dup = set(nums)
        if len(not_dup) < len(nums):
            return True
        else:
            return False
        