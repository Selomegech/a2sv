class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while n>1:
            x=n//2
            count = count + x
            
            n= n-x
        return count 
        