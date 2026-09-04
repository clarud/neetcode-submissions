class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand:
            return False

        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        hands = []
        hands.append([hand[0], 1])
        i = 1
        while i < len(hand):
            placed = False
            currCard = hand[i]
            for each in hands:
                if each[0] + 1 == currCard and each[1] < groupSize:
                    each[0] = currCard
                    each[1] += 1
                    placed = True
                    break

            if not placed:
                if len(hands) < (n // groupSize):
                    hands.append([currCard, 1])
                else:
                    return False
            i += 1
        end = all([items[1] == groupSize for items in hands])
        if end:
            return True
        return False