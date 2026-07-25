class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    """
    @param: str: a string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i

            # find the end of the integer
            while s[j] != "#":
                j += 1
            # how many following characters we have to read after j in order to get every character of the string
            length = int(s[i:j]) 

            # j is the delimiter so j+ 1 will be the 1st character of the string itself
            # j + 1 + length: length = how many characters we have to read after j, to get the every char of the string
            res.append(s[j + 1 : j + 1 + length])

            # go to the next string:
            # this is gonna be the beginning of the next string
            i = j + 1 + length 
        return res
