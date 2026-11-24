class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = "".join(sorted(s))
        t_string = "".join(sorted(t))

        if s_string == t_string:
            return True
        else:
            return False