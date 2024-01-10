class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0  # pointer for the name string
        j = 0  # pointer for the typed string

        while j < len(typed):
            # If both characters match, move both pointers forward
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            # If the typed character is the same as the previous name character, move only the typed pointer forward
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            # If none of the above conditions match, return False
            else:
                return False

        # If we have reached the end of the name string, but there are still characters in the typed string,
        # check if the remaining characters in the typed string are the same as the previous typed character
        while j < len(typed) and typed[j] == typed[j-1]:
            j += 1

        # If we have reached the end of both strings, it means all characters have been matched
        return i == len(name) and j == len(typed)