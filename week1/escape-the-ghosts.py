class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        begin=[0,0]
        x= (abs(target[0])-abs(begin[0])) + (abs(target[1])-abs(begin[1]))
        for i in range (len(ghosts)):
            N = abs(ghosts[i][0]-target[0]) + abs(ghosts[i][1]-target[1])
            if N <= x :
                return False
        return True  