class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted = ''
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                decrypted += chr(int(s[i:i + 2]) + 96)
                i += 3
            else:
                decrypted += chr(int(s[i]) + 96)
                i += 1
        
        return decrypted
        