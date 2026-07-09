class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        for i in range(len(nums)):
            res_prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    res_prod *= nums[j]
            res[i] = res_prod

        return res