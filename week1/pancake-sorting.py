class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        maximum = max(arr)

        def flip ( arr, m):
            n = 0
            
            while n < m :
                arr[n] , arr[m] = arr[m] , arr[n]
                n += 1
                m -= 1
            return (arr)

        
        while  maximum != 1:
            v= arr.index(maximum)
            flip (arr , v )
            result.append(v+1)
            flip(arr, maximum-1)
            result.append(maximum)

            maximum -= 1
            
        return (result) 
            


            
                    
        



        