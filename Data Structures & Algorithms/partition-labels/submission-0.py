class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        curr = set()
        counter = Counter(s)
        count = 0
        for char in s:
            if all(counter[each] == 0 for each in curr) and curr:
                res.append(count)
                curr = set()
                count = 0
            
            curr.add(char)
            counter[char] -= 1
            count += 1
        res.append(count)
        return res

            

