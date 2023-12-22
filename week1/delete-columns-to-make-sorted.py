class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        

        for i in range (len(strs[0])):
            sequence=[]
            # strs[i] = list(strs[0])
            for j in range (len(strs)):
                sequence.append(strs[j][i])
            sort = sorted(sequence)
            print(sort,sequence)
            
            if sort != sequence:
                count+=1
        return count 
                
                
        