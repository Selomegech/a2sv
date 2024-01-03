class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        n = len(processorTime) * 4
        processorTime.sort( reverse = True )
        result = []
        for i in range(len(tasks)):
            if (i+1) % 4 == 0 :
                # print(tasks[i])
                m = tasks[i] + processorTime[i//4]
                result.append(m)
        # print(result)
        return ( max(result))



        