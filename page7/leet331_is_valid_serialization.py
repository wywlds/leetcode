class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        def dfs(i):
            if i >= len(nodes):
                return False, len(nodes)
            if nodes[i] == '#':
                return True, i + 1
            valid, right_start = dfs(i + 1)
            if not valid:
                return False, len(nodes)
            valid, next_start = dfs(right_start)
            if not valid:
                return False, len(nodes)
            return True, next_start
        valid, next_start = dfs(0)
        if valid and next_start == len(nodes):
            return True
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
    print(solution.isValidSerialization("1,#"))
    print(solution.isValidSerialization("9,#,#,1"))