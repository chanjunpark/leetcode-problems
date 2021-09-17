class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = []
        for i in range(len(nums)):
            if i == 0:
                cache.append(nums[i])
            else :
                cache.append(max(0, cache[i-1]) + nums[i])
        return max(cache)