class Solution:
    def deckRevealedIncreasing(self, arr: List[int]) -> int:
        arr.sort(reverse = True)
        q = deque()
        i=0
        while i < len(arr):
            if len(q) != 0:
                x = q.pop()
                q.appendleft(x)
            q.appendleft(arr[i])
            i+=1
        return q
        