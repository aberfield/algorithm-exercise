class Solution {
    if ( x < 0) {
        return false;
    }
    int cur = 0;
    int num = x;
    while (n != 0) {
        cur = cur * 10 + num %10;
        num /= 10;
    }
    return cur == x;
}