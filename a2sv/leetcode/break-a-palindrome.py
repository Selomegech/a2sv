class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal =[]
        for i in palindrome:
            pal.append(i)

        if len(palindrome) == 1:
            return ('')
        for i in range(len(pal)//2):
            if pal[i] != 'a':
                n = ord('a') 
                pal[i] = chr(n)
                break
        else:
            pal[-1] = 'b'

        return ("" .join(pal))

         