class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Keep searching as long as the search range is valid
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Check if the target is present at mid
            if nums[mid] == target:
                return mid  # Target found, return its index
                
            # If target is smaller than mid, it can only be in the left half
            elif nums[mid] > target:
                right = mid - 1
                
            # If target is larger than mid, it can only be in the right half
            else:
                left = mid + 1

        # Target was not present in the array
        return -1