"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mem = {}
        for employee in employees:
            mem[employee.id] = (employee.importance, employee.subordinates)
        def dfs(id):
            if id not in mem:
                return 0
            imp, sub = mem[id]
            for s in sub:
                imp += dfs(s)
            return imp
        return dfs(id)