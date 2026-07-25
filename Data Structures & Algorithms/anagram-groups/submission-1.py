from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping the charCount of each string, to a list of Anagrams

        for s in strs: # go through every string we are given in the input

            # count how many of each character we have
            count = [0] * 26 # one for each character = a ..... z

            for c in s: # every single character in each string
                # count how many of each character

                """
                a = 80 -> 0, 80- 80
                b = 81 -> 1, 81 - 80
                """
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)
            
        return list(result.values())
