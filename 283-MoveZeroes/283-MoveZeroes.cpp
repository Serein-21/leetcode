// Last updated: 1/2/2026, 12:18:19 PM
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0; // Index to place the next non-zero element
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != 0) {
                swap(nums[i], nums[j]);
                i++; // Increment 'i' only when a non-zero element is found
            }
        }
    }
};
