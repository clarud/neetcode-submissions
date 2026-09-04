public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> groups = new Dictionary<string, List<string>>();
        foreach (string curr in strs) {
            char[] curr_chars = curr.ToCharArray();
            Array.Sort(curr_chars);
            string key = new string(curr_chars);
            if (!groups.ContainsKey(key)) {
                groups[key] = new List<string>([curr]);
            } else {
                groups[key].Add(curr);
            }
        }
        return new List<List<string>>(groups.Values);
    }
}
