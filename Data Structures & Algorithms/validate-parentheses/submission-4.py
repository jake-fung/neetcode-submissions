class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for c in s:
            if c in ['(', '{', '[']:
                res.append(c)
            elif len(res) > 0:
                if c == ')' and res[-1] == '(':
                    res.pop()
                elif c == '}' and res[-1] == '{':
                    res.pop()
                elif c == ']' and res[-1] == '[':
                    res.pop()
                else:
                    res.append(c)
            else:
                return False
        return len(res) == 0