class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left, right = 0, l - 1
        vol = 0
        leftmax, rightmax = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftmax = max(leftmax, height[left])
                vol += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                vol += rightmax - height[right]
        return vol