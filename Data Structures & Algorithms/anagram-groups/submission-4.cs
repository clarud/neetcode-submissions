public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> groups = new Dictionary<string, List<string>>();
        foreach (string curr in strs) {
            int[] counter = new int[26];
            foreach (char ch in curr) {
                int index = ch - 'a';
                counter[index]++;
            }
            string key = String.Join("#", counter);
            if (!groups.ContainsKey(key)) {
                groups[key] = new List<string>();
            }
            groups[key].Add(curr);
        }
        return groups.Values.ToList();
    }
}
