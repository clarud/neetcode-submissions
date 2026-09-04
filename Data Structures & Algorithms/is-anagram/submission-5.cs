public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }
        Dictionary<char, int> dict_s = new Dictionary<char, int>();
        foreach (char c in s) {
            if (!dict_s.ContainsKey(c)) {
                dict_s[c] = 1;
            } else {
                dict_s[c]++;
            }
        }
        foreach (char c in t) {
            if (!dict_s.ContainsKey(c) || dict_s[c] == 0) {
                return false;
            } else {
                dict_s[c]--;
            }
        }

        return true;
    }
}
