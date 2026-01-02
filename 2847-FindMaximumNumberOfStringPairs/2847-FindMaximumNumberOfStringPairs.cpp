// Last updated: 1/2/2026, 12:17:24 PM
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int pair = 0;

        for (int i = 0; i < words.size() - 1; i++) {
            for (int j = i + 1; j < words.size(); j++) {  // Iterate from 'i + 1' 
                string reversedWord = words[j];  // Store a copy
                reverse(reversedWord.begin(), reversedWord.end()); 
                if (words[i] == reversedWord) {
                    pair++; 
                }
            }
        }

        return pair;
    }
};
