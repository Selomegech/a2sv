class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        goods=set()
        equals=set()
        result= set()
        for i in range (len(fronts)):
            if fronts[i]!=backs[i]:
                goods.add(fronts[i])
                goods.add(backs[i])
            else:
                equals.add(fronts[i])
        if goods:
            result= goods - equals 
        if result :
            return (min(result)) 
        else:
            return 0 
            
                
                
         
        
                
                
       
        

        

            
        
        
        