// Last updated: 1/2/2026, 12:17:20 PM
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> output;
        for (int i = 0; i < words.size(); i++) {
            string f = words[i]; 
            for (int j = 0; j < f.length(); j++) { 
                if (f[j] == x) {
                    output.push_back(i);
                    break; // Stop checking the rest of the word
                }
            }   
        }
        return output;
    }
};
