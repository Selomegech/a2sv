class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dictionary = defaultdict()
        same_count = 0
        move = 0.1
        for i in range(len(points)):
            distance = sqrt((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2)
            if distance not in dictionary:
                dictionary[distance] = points[i]
            else:
                print(points[i])
                dictionary[distance + move] = points[i]
                move += 0.1


        # dictionary.sort( key = distance )
        sorted_dict = OrderedDict(sorted(dictionary.items()))
        result = []
        print(sorted_dict)
        
        for key , value in sorted_dict.items():
            result.append(value)
        res=[]
        i=0
        while len(result) >= k and i < k :
            res.append(result[i])
            i += 1
        return(res)


        