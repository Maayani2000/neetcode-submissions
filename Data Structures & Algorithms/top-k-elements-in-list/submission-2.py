class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creates an object with automatically counts all the occurences
        count = Counter(nums)
        
        most_common_items = count.most_common(k)

        # item[0] - the keys only (the numbers)
        return [item[0] for item in most_common_items]
