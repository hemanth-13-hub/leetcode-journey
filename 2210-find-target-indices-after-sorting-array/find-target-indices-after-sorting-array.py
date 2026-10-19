class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new_array=[]
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i]==target:
                new_array.append(i)
        return new_array
        