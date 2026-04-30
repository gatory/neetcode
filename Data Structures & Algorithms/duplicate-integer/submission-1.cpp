class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (!nums.empty()){
            for(int i = 0 ; i <= nums.size(); i++) {
                for (int j = i + 1 ; j <= nums.size() - 1 ; j++) {
                    if (nums[i] == nums[j]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
