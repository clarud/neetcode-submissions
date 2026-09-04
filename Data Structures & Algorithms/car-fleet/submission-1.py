class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        remain_time = [((target - p) / s, p)for p, s in zip(position, speed)]
        remain_time.sort(key=lambda x: -x[1])
        time = remain_time[0][0]
        print(remain_time)
        for tr, p in remain_time:
            if tr > time:
                res += 1
                time = tr
        return res