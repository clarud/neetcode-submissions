class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        ordered = sorted(counter)
        for card in ordered:
            times = counter[card]
            for i in range(groupSize):
                counter[card + i] -= times
                if counter[card + i] < 0:
                    return False
        return True
        