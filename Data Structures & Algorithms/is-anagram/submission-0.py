class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countT = {}
        countS = {}

        for index in range(len(s)):
            countT[t[index]] = countT.get(t[index], 0) + 1
            countS[s[index]] = countS.get(s[index], 0) + 1

        if countT == countS:
            return True

        return False


        