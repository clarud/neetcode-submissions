class Solution:
    def helper(self, index: int, current: List[int]) -> None:
        if sum(current) == self.target:
            if current not in self.res:
                self.res.append(current)
        if index >= len(self.candidates):
            return
        current.append(self.candidates[index])
        self.helper(index + 1, current[:])
        current.pop()
        self.helper(index + 1, current[:])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.target = target
        candidates.sort()
        self.candidates = candidates
        self.helper(0, [])
        return self.res