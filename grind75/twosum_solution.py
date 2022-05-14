class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            complement = target-nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    return i,j
# This is the brute force/ naive way of approaching this problem, you start at the first number and check to see if its complement
# exists within the array, if so return i,j
# The time complexity of this is Theta n^2 in the length of the list, the space complexity is Theta 1

# I know for certain we can do better in terms of our time complexity but it is going to come at the cost of space
class Solution(object):
    def twoSum_htable(self, nums, target):
        htable = {} #key-value pari
        for idx, value in enumerate(nums): #we need to get the index and the actual number value
            complement = target - value
            if complement in htable:
                return (htable[complement], idx)
            htable[value] = idx
# This is a hash table solution. We check if the complement is in the hashtable otherwise we insert that value into the hashtable
# When we find the complement we return the position of htable and idx
