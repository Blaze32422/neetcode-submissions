class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        m = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] += 1
            else:
                h[s[i]] = 1
            if t[i] in m:
                m[t[i]] += 1
            else:
                m[t[i]] = 1
            
        return m == h


