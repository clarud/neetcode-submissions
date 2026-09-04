public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = new Dictionary<int, int>();
        int i = 0;
        foreach (int num in nums) {
            if (seen.ContainsKey(target - num)) {
                return [seen[target - num], i];
            }
            seen[num] = i;
            i++;
        }
        return [-1, -1];
    }
}
