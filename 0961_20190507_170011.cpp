class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        char cur = name[0];
        const char *pn = name.c_str(), *pt = typed.c_str();
        int cnt = 0;
        while(true) {
            if(*pn != 0 && cur == *pn) {
                ++cnt;
                ++pn;
            } else {
                while(*pt != 0 && *pt == cur) {
                    ++pt;
                    --cnt;
                }
                if(cnt > 0) return false;
                if(*pt == 0) return (*pn == 0);
                cnt = 0;
                cur = *pn;
            }
        }
        assert(false);
    }
};