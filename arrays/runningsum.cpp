class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        // For this loop we want to iterate from index position 1 as we are going to use add the lagging value
        for(int i = 1; i < nums.size(); i++){
            // the running sum should be the value at the current position + the position i-1
            nums[i] = nums[i] + nums[i-1];
        } return nums;
     }
};

// For runtime complexity this is ideal in O(N)
// For memory usage not perfect, 8.5 mb could be better
