class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {} # value : index
        for i, n in enumerate(nums):
            difference = target - n
            if difference in dictionary:
                return [dictionary[difference], i]
            dictionary[n] = i