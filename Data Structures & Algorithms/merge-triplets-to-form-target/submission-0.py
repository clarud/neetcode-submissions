class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filteredTriplets = []
        res = [False, False, False]
        for triplet in triplets:
            first, second, third = triplet
            firstTarget, secondTarget, thirdTarget = target
            if first > firstTarget or second > secondTarget or third > thirdTarget:
                continue
            else:
                filteredTriplets.append(triplet)
        for triplet in filteredTriplets:
            first, second, third = triplet
            firstTarget, secondTarget, thirdTarget = target
            if first == firstTarget:
                res[0] = True
            if second == secondTarget:
                res[1] = True
            if third == thirdTarget:
                res[2] = True
        return False not in res