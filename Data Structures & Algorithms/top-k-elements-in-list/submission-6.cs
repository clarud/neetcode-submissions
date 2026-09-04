public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> counter = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (!counter.ContainsKey(num)) {
                counter[num] = 0;
            }
            counter[num]++;
        }
        List<KeyValuePair<int, int>> freq_list = counter.ToList();
        freq_list.Sort((a,b) => b.Value.CompareTo(a.Value));
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = freq_list[i].Key;
        }
        return res;
    }
}
