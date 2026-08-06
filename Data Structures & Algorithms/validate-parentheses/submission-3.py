class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        brackets_dict = {'(':')','{':'}','[':']'}
        for bracket in s:
            if bracket in brackets_dict:
                open_brackets.append(bracket)
            elif open_brackets:
                open_bracket = open_brackets.pop()
                close_bracket = brackets_dict[open_bracket]
                if close_bracket!=bracket:
                    return False
            else:
                return False
        if len(open_brackets)!=0:
            return False
        return True
