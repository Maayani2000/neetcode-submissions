class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        k_frequent = []
    
        for i in nums:
            if i not in temp:
                temp[i] = 1
            else:
                temp[i] += 1
                
        unique_numbers = list(temp.keys())
        unique_numbers.sort(key=lambda x: temp[x], reverse=True)

        for i in range(k):
            k_frequent.append(unique_numbers[i])
        return k_frequent