# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        for i in range(n):
            k = pairs[i].key
            for j in range(i + 1):
                if k >= pairs[j].key:
                    continue
                tmp = pairs[i]
                for x in range(i, j, -1):
                    pairs[x] = pairs[x - 1]
                pairs[j] = tmp
                break
            res.append(pairs[:])
        return res