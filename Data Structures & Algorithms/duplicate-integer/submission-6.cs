public class Solution {
    public bool hasDuplicate(int[] nums) {
        if (nums.Length == 0) {
            return false;
        }
        Array.Sort(nums);
        int current = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (current == nums[i]) {
                return true;
            }
            current = nums[i];
        }
        return false;
    }
}