class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        for i in range(l):
            maxi= max(nums[0:i+1])
            mini = min(nums[i:l])

            if maxi-mini <=k:
                return i

        return -1
            