class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Map closing brackets to their corresponding opening brackets
        brackets_map = {")": "(",
                        "}" : "{",
                        "]": "["}
        stack = []
        
        # 2. Iterate through every character in the string
        for char in s:
            # If it's a closing bracket
            if char in brackets_map:
                # Check if stack is empty before popping to prevent crash
                if not stack:
                    return False
                
                top_element = stack.pop()
                
                # Check if the opening bracket matches
                if brackets_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # 3. If the stack is empty, all brackets were properly matched
        return len(stack) == 0