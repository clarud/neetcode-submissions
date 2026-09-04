class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        pre = [0] * l
        post = [0] * l
        pre[0] = height[0]
        for i in range(1, l, 1):
            pre[i] = max(pre[i - 1], height[i])
        post[l - 1] = height[l - 1]
        for j in range(l - 2, -1, -1):
            post[j] = max(post[j + 1], height[j])

        res = 0
        for i in range(l):
            res += min(pre[i], post[i]) - height[i]
        return res