class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        sort(num.begin(), num.end());
        unsigned int count = 1;
        unsigned int maxCount = 1;
        for (int i = 1; i < num.size(); ++i) {
            if (num[i] == num[i - 1] + 1) {
                count++;
            }
            else if (num[i] != num[i - 1]) {
                if (count > maxCount) {
                    maxCount = count;
                }
                count = 1;
            }
            else {
            }
        }
        if (count > maxCount) {
            maxCount = count;
        }
        return maxCount;
    }
private:
    char* mem;
    unsigned int ConvertToUINT(int num)
    {
        return static_cast<unsigned int>(num) + 0x80000000;
    }
    
};