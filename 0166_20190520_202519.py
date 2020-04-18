from collections import OrderedDict
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, d = numerator, denominator
        is_neg = (n < 0) ^ (d < 0) and n != 0
        n = -n if n < 0 else n
        d = -d if d < 0 else d
        
        int_part = str(n //d)
        r = n % d
        if r == 0:
            return '-' + int_part if is_neg else int_part

        point_part = OrderedDict()
        while r:
            nr = r * 10
            q = nr // d
            point_part[r] = str(q)
            r = nr % d
            if r in point_part:
                break
        else:
            return f'{"-" if is_neg else ""}{int_part}.{"".join(point_part.values())}'

        ans = f'{int_part}.'
        for r_, q in point_part.items():
            if r_ == r:
                ans += '('
            ans += q
        ans += ')'
        return '-' + ans if is_neg else ans
