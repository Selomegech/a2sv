class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        result = [0] * (n1 + n2)
        
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2
                
                pos1 = i + j
                pos2 = i + j + 1
                sum_val = product + result[pos2]
                
                result[pos1] += sum_val // 10
                result[pos2] = sum_val % 10
        
        # Remove leading zeros
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        
        if i == len(result):
            return "0"
        
        return ''.join(map(str, result[i:]))