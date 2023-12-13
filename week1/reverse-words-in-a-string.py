class Solution:
    def reverseWords(self, s: str) -> str:
        result=[]
        lists = list(s.split())
        lists.reverse()
        result= " ".join(lists)
        return result

        