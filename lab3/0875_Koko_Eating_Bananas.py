class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left