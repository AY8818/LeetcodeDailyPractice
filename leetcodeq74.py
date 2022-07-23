def combinationSum(candidates,target):
    candidates.sort()
    lst = []
    def dfs(index,target,n,temp):
        if target == 0:
            lst.append(temp[:])
            return
        for i in range(index,len(candidates)):
            if target - candidates[i] < 0:
                return
            temp.append(candidates[i])
            dfs(i,target-candidates[i],n+1,temp)
            temp.pop()

    dfs(0,target,0,[])
    return lst

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(candidates,target))
