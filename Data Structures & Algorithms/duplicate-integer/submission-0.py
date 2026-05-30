class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        our_hash = set()
        for i in nums:
            if i in our_hash:
                return True
            else:
                our_hash.add(i)
        return False