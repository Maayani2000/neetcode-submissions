class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        you can't rob adjacent houses on the same night
        """
        odd_sum = sum(nums[0::2])
        even_sum = sum(nums[1::2])
        
        return max(odd_sum, even_sum)