class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKth(a, b, k):
            k = int(k)
            if not a:
                return b[k - 1]
            if not b:
                return a[k - 1]
            if k == 1:
                return min(a[0], b[0])
            i = min(len(a), int(k // 2))
            j = min(len(b), int(k // 2))

            if a[i - 1] <= b[j - 1]:
                return getKth(a[i:], b, k - i)
            else:
                return getKth(a, b[j:], k - j)
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return getKth(nums1, nums2, (total + 1) / 2)
        else:
            return ((getKth(nums1, nums2, total / 2) + getKth(nums1, nums2, total / 2 + 1)) / 2.0)

        
