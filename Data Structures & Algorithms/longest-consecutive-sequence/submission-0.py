class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        size = 0
        i = 0
        while i < len(nums):
            if (nums[i] - 1) not in nums:
                target = nums[i]+1
                n = 1
                while target in nums:
                    n+=1
                    target += 1
                if n > size:
                    size = n
            i += 1

        return size