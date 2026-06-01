class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr_nums, perm):
            if not curr_nums:
                res.append(perm)
                return
            for i in range(len(curr_nums)):
                next_nums = curr_nums[:i] + curr_nums[i+1:]
                dfs(next_nums, perm + [curr_nums[i]])
        dfs(nums, [])
        return res