
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for shift in (shifts):
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1
                prefix[shift[1] + 1] -= 1
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        res = []
        for i in range (len(prefix) - 1):
            
            prefix[i] = prefix[i] % 26
        
            if (ord(s[i]) + prefix[i]) < 97:
                output = (ord(s[i]) + prefix[i]) + 26
                res.append(chr(output))  
            elif (ord(s[i]) + prefix[i]) > 122:
                output = (ord(s[i]) + prefix[i]) - 26
                res.append(chr(output)) 
            else:
                output = ord(s[i]) + prefix[i]
                res.append (chr(output))
        return "".join(res)
        