class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringx = str(x)
        if stringx[::-1] == stringx:
            return True
        else:
            return False
# how can we improve the initial brute force solution
# we don't need to allocate memory for stringx
# we shouldn't need a conditional either, since we are just returning a boolean value we should just be able to return the value of the equality


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
# are their any additional improvements we can make to this
# we didn't allocate additional memory for any variables 
# hypothetically we could use a conditional to check if x is greater than 0 to return faster if we wanted to account for negatives immediately
# this depending on knowledge of the data could be an improvement

# there are some really cool suggestions online about reversing the number without converting it to a string which really improves runtime

# so this one has to do with reversing the number itself by using mod 10 
# the first conditional returns false is the number is negative or ends in a 0
# if result//10 == x we return true because this will ignore the middle digit of the original number
# it ended up not running as fast as I thought it would but still a really cool solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0) or (x > 0 and x %10==0):
            return False
        result = 0
        while(x > result):
            result = result*10+x%10
            x = x//10
        return True if(x == result or x ==result//10) else False
