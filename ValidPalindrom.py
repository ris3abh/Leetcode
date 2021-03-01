class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:          return True
        h, t = 0, len(s)-1
        while h < t:
            if not s[h].isalnum(): h += 1
            elif not s[t].isalnum():t -= 1
            else:
                if s[h].lower() == s[t].lower():
                    h += 1
                    t -= 1
                else:
                    return False
        return True