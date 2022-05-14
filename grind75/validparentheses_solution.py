class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # So the first thing I'm thinking about is what base cases can we just automatically return
        if(len(s) < 2 or len(s) % 2 == 1):
            return False
        new_stack = []
        for element in s:
            if(element == '(' or element == '{' or element == '['):
                new_stack.append(element)
            else:
                if len(new_stack) == 0:
                    return False
                latest_element = new_stack.pop()
                if(
                    ( latest_element == '(' and element != ')') or
                    ( latest_element == '{' and element != '}') or 
                    ( latest_element == '[' and element != ']')
                ): return False
        return len(new_stack) == 0
