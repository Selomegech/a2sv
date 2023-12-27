class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range (len(names)):
            pos=i
            for j in range (i+1,len(names)):
                
                if heights[pos] < heights[j]:
                    pos= j
            if pos!= i:
                names[i],names[pos]= names[pos],names[i]
                heights[i],heights[pos]= heights[pos],heights[i]
        return names


                

            
        
        