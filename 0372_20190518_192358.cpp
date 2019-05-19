class Solution {
public:
    int superPow(int a, vector<int>& b) {
        int ans = 1;
        int m = 1337;
        a %= m;
        int base = a;
        for(auto iter = b.rbegin(); iter != b.rend(); ++iter) {
            ans *= modPow(base, *iter, m);
            ans %= m;
            base = modPow(base, 10, m);
        }
        return ans;
    }
    
    int modPow(int a, int b, int m) {
        unsigned int mask = 1;
        a = a % m;
        int tmp = 1;
        while (mask <= b) mask <<= 1;
        if (mask == 0x80000000) mask = 0x40000000;
        else mask >>= 1;
        while (mask) {
            tmp *= tmp;
            tmp %= m;
            if (mask & b) {
                tmp *= a;
                tmp %= m;
            }
            mask >>= 1;
        }
        return tmp;
    }
};