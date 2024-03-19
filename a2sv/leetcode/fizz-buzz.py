class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        outputList = []
        for i in range(1,n + 1):
            if i % 15 == 0:
                outputList.append("FizzBuzz")
            elif i % 3 == 0:
                outputList.append("Fizz")
            elif i % 5 == 0:
                outputList.append("Buzz")
            else:
                outputList.append(str(i))
        return outputList