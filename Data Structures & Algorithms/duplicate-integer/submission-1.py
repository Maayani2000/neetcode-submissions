class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        integer array - nums
        return true if any value appears more than once in the array, otherwise false

        set(nums) removes duplicates automatically. 
        so if the length of the original array is different than the len of set(nums),
        then it contains duplicates
        """
        return len(nums) != len(set(nums))