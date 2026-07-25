class Solution:

    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = []
        answer.append(self.distinctOfList(nums1, nums2))
        answer.append(self.distinctOfList(nums2, nums1))
        return answer 

    def distinctOfList(self, nums1: list[int], nums2: list[int]) -> list[int]:
        distincts = set() # set - prevents duplicates
        set2 = set(nums2) # a search in set() is o(1)

        for i in nums1:
            if i not in set2:
                distincts.add(i)

        return list(distincts)