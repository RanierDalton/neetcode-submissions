class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_table, t_table = {}, {}
        for s_letter, t_letter in zip(s, t):
            s_table[s_letter] = s_table.get(s_letter, 0) + 1
            t_table[t_letter] = t_table.get(t_letter, 0) + 1

        return s_table == t_table
