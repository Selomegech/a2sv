class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s: str, i: int) -> Tuple[str, int]:
            decoded_string = ""
            k = 0

            while i < len(s):
                if s[i].isdigit():
                    k = k * 10 + int(s[i])
                elif s[i] == '[':
                    nested_string, i = helper(s, i + 1)
                    decoded_string += nested_string * k
                    k = 0
                elif s[i] == ']':
                    return decoded_string, i
                else:
                    decoded_string += s[i]
                i += 1

            return decoded_string, i

        result, _ = helper(s, 0)
        return result