class Solution:
    def smallestNumber(self, num: int) -> int:
        number_str = str(num)
        digits = []
        string = list(number_str)
        if string[0]=='-':
            string[1:] = sorted(string[1:] , reverse= True) 
            return int(''.join(string)) 
        string.sort()
        
        

        if string[0] == '0':
        
            for i in range(len(string)):
                if string[i] != "0":
                    string[0] , string[i] = string[i] , string[0]
                    break
            
            
        result = ''.join(string)
        return(int(result))
                



        