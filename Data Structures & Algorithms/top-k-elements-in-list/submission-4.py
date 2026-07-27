from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1

        sorted_dict = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[:k]