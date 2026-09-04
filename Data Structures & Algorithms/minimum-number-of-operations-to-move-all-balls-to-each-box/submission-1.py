class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        balls = 0
        moves = 0

        for i in range(n):
            result[i] += moves
            balls += int(boxes[i])
            moves += balls
        
        balls = 0
        moves = 0

        for i in range(n - 1, -1, -1):
            result[i] += moves
            balls += int(boxes[i])
            moves += balls
        return result