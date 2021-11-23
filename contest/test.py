def subsets(strs):
    res = []
    temp = []
    def backtrack(strs, temp, pos):
        res.append(temp[:])
        for i in range(pos, len(strs)):
            if i > pos and strs[i] == strs[i-1]:
                continue
            temp.append(strs[i])
            backtrack(strs, temp, i+1)
            temp.pop()

    backtrack(strs, temp, 0)
    return res


if __name__=="__main__":
    print(subsets(['a', 'a', 'b', 'c']))