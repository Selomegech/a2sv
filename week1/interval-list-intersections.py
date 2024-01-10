class Solution:
    def intervalIntersection(self, firstList, secondList):
        result = []
        i = 0  # pointer for the firstList
        j = 0  # pointer for the secondList

        while i < len(firstList) and j < len(secondList):
            # Find the intersection of the intervals
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            # If the intersection is valid (start <= end), add it to the result
            if start <= end:
                result.append([start, end])

            # Move the pointers based on the interval that has the smaller endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result