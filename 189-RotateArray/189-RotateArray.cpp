// Last updated: 1/2/2026, 12:18:35 PM
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; // Handle cases where k is larger than the array size

        vector<int> temp(n);  // Create a temporary array
        for (int i = 0; i < n; i++) {
            temp[(i + k) % n] = nums[i];
        }

        nums = temp;  // Copy rotated elements back to the original array
    }
};
