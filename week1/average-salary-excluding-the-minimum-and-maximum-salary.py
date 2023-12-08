class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float('inf')
        maxSalary = float('-inf')
        totalSalary = 0
        employeeCount = 0
        
        for s in salary:
            minSalary = min(minSalary, s)
            maxSalary = max(maxSalary, s)
        
        for s in salary:
            if s != minSalary and s != maxSalary:
                totalSalary += s
                employeeCount += 1
        
        return totalSalary / employeeCount