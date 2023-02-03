#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    bool isAlienSorted(vector<string> &words, string order) {
        //define hashmap
        unordered_map<char, int> lookup;
        int orderN = order.size();
        for (int i = 0; i < orderN; i++) {
            int index = i + 1;
            char character = order[i];
            lookup[character] = index;
        }

        // assumption: word1 < word2
        auto checkOrder = [&](string word1, string word2) {
            //word1 is small
            int N1 =  word1.size();
            int N2 = word2.size();

            for (int i = 0; i < N1; i++) {
                if (i >= N2) {
                    break;
                }

                if (word1[i] == word2[i]) {
                    continue;
                }

                int num1 = lookup[word1[i]];
                int num2 = lookup[word2[i]];

                if (num1 > num2) {
                    return false;
                }

                return true;
            }

            if (N1 > N2) {
                return false;
            }

            return true;
        };

        int wordN = words.size();

        for (int i = 1; i < wordN; i++) {
            string w1 = words[i - 1];
            string w2 = words[i];

            if (!checkOrder(w1, w2)) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    Solution s;
    vector<string> words = {"hello", "leetcode"};
    string order = "hlabcdefgijkmnopqrstuvwxyz";
    // order = "abcdefghijklmnopqrstuvwxyz"
    bool res = s.isAlienSorted(words, order);
    cout << "This is the result: " << res << endl;
    return 0;
}
