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

#This is my first solution here I use a stack
#I can do a little bit better

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening_braces = set('{[(')
        close_to_open = { '}':'{', ')':'(', ']':'[' }
        stack = []
        for element in s:
            if element in opening_braces:
                stack.append(element)
            else: 
                if len(stack)==0 or stack[-1]!= close_to_open[element]:
                    return False
                stack.pop()
        return len(stack) == 0
