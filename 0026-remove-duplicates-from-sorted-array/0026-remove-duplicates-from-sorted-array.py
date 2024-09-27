class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for index in range(1, len(nums)):
            if nums[index - 1] != nums[index]:
                nums[k] = nums[index]
                k += 1
        
        return k
