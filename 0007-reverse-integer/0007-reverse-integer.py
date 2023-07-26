class Solution:
    def reverse(self, x: int) -> int:
        x_list = list(str(x))
        sign = '+'
        if x_list [0] == '-':
            sign, x_list = '-', x_list[1:]
        x_list = reversed(x_list)
        ret = int(''.join(x_list))
        ans = ret if sign == '+' else -1*ret
        return ans if -1*2**31<=ans<2**31 else 0