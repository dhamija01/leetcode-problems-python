class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        
        prefix_max= [0]*l
        prefix_max[0]= nums[0]
        for i in range(1,l):
            prefix_max[i]= max(prefix_max[i-1],nums[i])


        suffix_min = [0]*l
        suffix_min[l-1]=nums[l-1]
        for i in range(l-2,-1,-1):
            suffix_min[i] = min(suffix_min[i+1],nums[i])

        
        for i in range(l):
            if prefix_max[i] - suffix_min[i] <= k:
                return i

        return -1