from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1  # impossible overall

        # Build signed segments: (start_index, sum)
        segs = []
        i = 0
        while i < n:
            if diff[i] == 0:
                # treat zeros as their own (non-negative) mini-segment
                segs.append((i, 0))
                i += 1
                continue
            s = i
            total = diff[i]
            sign = 1 if diff[i] > 0 else -1
            i += 1
            while i < n and (diff[i] > 0) == (sign > 0) and diff[i] != 0:
                total += diff[i]
                i += 1
            segs.append((s, total))

        # Merge adjacent non-negative segments (to reduce fragmentation by zeros)
        merged = []
        for s, val in segs:
            if merged and merged[-1][1] >= 0 and val >= 0:
                ms, mv = merged.pop()
                merged.append((ms, mv + val))
            else:
                merged.append((s, val))
        segs = merged

        m = len(segs)
        if m == 1:
            # Only one segment; if total >= 0, start at its start.
            return segs[0][0] if segs[0][1] >= 0 else -1

        # Two-pointer over segments on a circle:
        # Try to find a non-negative segment that can absorb all following deficits.
        # We’ll walk at most 2*m segments total → O(m) ≤ O(n).
        start_idx = 0
        # Advance start_idx to the first non-negative segment
        while start_idx < m and segs[start_idx][1] < 0:
            start_idx += 1
        if start_idx == m:
            return -1  # all segments negative, but total>=0 would have caught this earlier

        curr = segs[start_idx][1]
        taken = 1
        j = (start_idx + 1) % m

        while taken < m:
            curr += segs[j][1]
            if curr < 0:
                # fail: discard the current start segment; move start to next non-negative segment after j
                start_idx = (j + 1) % m
                # skip negatives until we hit a non-negative segment, or wrap
                hopped = 0
                while hopped < m and segs[start_idx][1] < 0:
                    start_idx = (start_idx + 1) % m
                    hopped += 1
                if hopped == m:
                    return -1
                curr = segs[start_idx][1]
                taken = 1
                j = (start_idx + 1) % m
            else:
                taken += 1
                j = (j + 1) % m

        # We consumed all segments without dipping below zero → start_idx’s segment works.
        return segs[start_idx][0]
