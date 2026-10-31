class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


    # solution T(O)-> N*2
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j]== target:
    #                 return i,j



        storehash={}

        for i,val in enumerate(nums):
            sub= target-val
            if sub in storehash:
                return [storehash[sub],i]
            storehash[val]=i