class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def helper(i, j, m, turn):
            print(f"{i}, {j}, {m}, {turn}")
            if m == len(s3):
                if i != len(s1) or j != len(s2):
                    return False
                return True
            if ((i == len(s1) and turn == 1) or (j == len(s2) and turn ==2)):
                return False
            if turn == 1:
                tmp = i
                while i < len(s1) and m < len(s3) and s1[i] == s3[m]:
                    i += 1
                    m += 1
                if i == tmp:
                    return False
                return helper(i, j, m, 2)
            else:
                tmp = j
                while j < len(s2) and m < len(s3) and s2[j] == s3[m]:
                    j += 1
                    m += 1
                if j == tmp:
                    return False
                return helper(i, j, m, 1)

        return helper(0, 0, 0, 1) or helper(0, 0, 0, 2)