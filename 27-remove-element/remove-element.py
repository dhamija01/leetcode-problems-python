class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 =0 
        l= len(nums)
        for i in range(l):
            if nums[i] != val:
                nums[p1] = nums[i]  
                p1 +=1
        return p1