from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together in O(N * K log K) time complexity.
        
        N = number of strings, K = maximum length of a string.

        How it works:
        1. Uses a 'defaultdict(list)' to avoid checking if a key exists before appending.
        2. Words that are anagrams share the exact same sorted character sequence (e.g., "eat" and "tea" -> "aet").
        3. Sets the sorted string as the map key and appends the original word to its list.
        4. Returns all grouped lists.
        """
        # Group list initialized automatically for new keys
        ans = defaultdict(list)

        for word in strs:
            # Sort the word to create a common key for all its anagrams
            sorted_word = "".join(sorted(word))
            ans[sorted_word].append(word)

        return list(ans.values())