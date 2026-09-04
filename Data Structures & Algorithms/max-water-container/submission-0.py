class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0
        while l < r:
            dist = r - l
            vol = min(heights[l], heights[r]) * dist
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] >= heights[l]:
                l += 1
            max_vol = max(vol, max_vol)
        return max_vol