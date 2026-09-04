class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * l
        postfix = [1] * l
        res = []
        for i in range(l):
            if i == 0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(l - 1, -1, -1):
            if i == l - 1:
                postfix[i] = nums[i]
                continue
            postfix[i] = postfix[i + 1] * nums[i]

        for i in range(l):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == l - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
            
        return res