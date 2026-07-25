class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        k = len(p)
        
        for i in range(len(s) - k + 1):
            sub = s[i : i + k]
            if self.isAnagram(sub, p):
                result.append(i)
                
        return result

    def isAnagram(self, s: str, p: str) -> bool:
        return Counter(s) == Counter(p)
