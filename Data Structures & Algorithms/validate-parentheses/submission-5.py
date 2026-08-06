class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        open_brackets = []
        brackets_dict = {'(':')','{':'}','[':']'}
        for bracket in s:
            if bracket in brackets_dict:
                open_brackets.append(bracket)
            elif open_brackets:
                close_bracket = brackets_dict[open_brackets.pop()]
                if close_bracket!=bracket:
                    return False
            else:
                return False
        if len(open_brackets)!=0:
            return False
        return True
