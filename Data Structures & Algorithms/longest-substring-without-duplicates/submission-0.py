class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores: {character: last_seen_index}
        max_length = 0
        left = 0  # Left pointer of the sliding window

        for right in range(len(s)):
            current_char = s[right]

            # If the character is repeated and is inside the current window
            if current_char in char_map and char_map[current_char] >= left:
                # Move the left pointer past the last seen position of this character
                left = char_map[current_char] + 1

            # Update the last seen index of the current character
            char_map[current_char] = right

            # Calculate current window size and update max_length
            current_window_len = right - left + 1
            if current_window_len > max_length:
                max_length = current_window_len

        return max_length