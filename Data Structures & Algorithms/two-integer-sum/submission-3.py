class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Solution 1 - Naive

        n = len(nums)
        for i in range(n):
            # Inner loop picks the second number (starting exactly after the first one)
            for j in range(i + 1, n):
                # Check if their sum equals the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        """

        # Solution 2 - Hash map
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]    
            seen[num] = i
        return []
      