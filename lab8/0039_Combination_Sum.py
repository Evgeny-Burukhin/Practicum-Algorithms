class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, curr_sum, combo):
            if curr_sum == target:
                res.append(combo)
                return
            if curr_sum > target or idx >= len(candidates):
                return
            dfs(idx, curr_sum + candidates[idx], combo + [candidates[idx]])
            dfs(idx + 1, curr_sum, combo)
        dfs(0, 0, [])
        return res