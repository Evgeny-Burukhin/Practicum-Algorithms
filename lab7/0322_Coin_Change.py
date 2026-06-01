class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for curr in range(1, amount + 1):
            for coin in coins:
                if curr - coin >= 0:
                    dp[curr] = min(dp[curr], 1 + dp[curr - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1