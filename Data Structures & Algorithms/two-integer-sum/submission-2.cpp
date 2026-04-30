class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0 ; i < nums.size() ;i++) {
            int diff = target - nums.at(i);
            for (int j = i ; j < nums.size() ;j++) {
                if (nums.at(j) == diff && j != i) {
                    vector<int> ans = {i, j};
                    return ans;
                }
            }
        }
    }
};
