class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        if sum(diff) < 0:
            return -1

        fuel = 0
        start = 0
        end = 0
        taken = 0

        while taken < n:
            fuel += diff[end]
            end = (end + 1) % n
            taken += 1
            while fuel < 0:
                fuel -= diff[start]
                start = (start + 1) %n
                taken -= 1
        return start

            


        

