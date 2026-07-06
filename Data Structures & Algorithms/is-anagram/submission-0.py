class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_dict = {}
        s2_dict = {}

        for i in s:
            if i in s1_dict:
                s1_dict[i] += 1
            else:
                s1_dict[i] = 1

        for i in t:
            if i in s2_dict:
                s2_dict[i] += 1
            else:
                s2_dict[i] = 1

        if s1_dict == s2_dict:
            return True
        else:
            return False