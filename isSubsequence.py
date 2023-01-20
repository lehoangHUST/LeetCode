class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
            Cách làm c?a bài toán này nhu sau:
            + Ki?m tra xem các kí t? c?a chu?i s có n?m trong chu?i t hay không ?
        """
        for s_i in s:
            if s_i not in t:
                return False
        
        # L?y ph?n t? position
        position_chars = []
        for s_i in s:
            for index, t_i in enumerate(t):
                if s_i == t_i and index not in position_chars:
                    position_chars.append(index)
        
        position_chars.sort()
        chars = []
        for position_char in position_chars:
            chars.append(t[position_char])

        
        if len(s) == len(chars):
            return True if s == ''.join(chars) else False
        else:
            if len(s) > len(chars):
                return False
            else:
                index = 0
                for i, char in enumerate(chars):
                    if chars[i] == s[index]:
                        index += 1
                    
                    if index >= len(s):
                        break

                if index == len(s):
                    return True
                else:
                    return False