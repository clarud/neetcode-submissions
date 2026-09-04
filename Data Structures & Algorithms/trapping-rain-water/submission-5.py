class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left, right = 0, l - 1
        res = 0
        maxleft, maxright = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                res += maxleft - height[left]
                left += 1
                maxleft = max(maxleft, height[left])
            else:
                res += maxright - height[right]
                right -= 1
                maxright = max(maxright, height[right])
        return res