public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        foreach (int num in nums) {
            seen.Add(num);
        }
        if (seen.Count == nums.Length) {
            return false;
        } else {
            return true;
        }
    }
}