class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        splitted_s1 = s1.split()
        splitted_s2 = s2.split()

        # Combine results from both directions into a single list
        res = self.uncommonCheck(splitted_s1, splitted_s2)

        # append() = add the obj as is, as a single variable at the end of the list
        # extend() = go through the given obj, and add to its end each variable, separately
        res.extend(self.uncommonCheck(splitted_s2, splitted_s1))

        return res
        
    def uncommonCheck(self, s1: List[str], s2: List[str]) -> List[str]:
        res = []
        for word in s1:
            # Word must appear exactly once in s1 and zero times in s2
            if s1.count(word) == 1 and word not in s2:
                res.append(word)
        return res
