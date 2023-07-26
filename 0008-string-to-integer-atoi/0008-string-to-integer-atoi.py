class Solution:
    def myAtoi(self, s: str) -> int:
        sign, ret, flag = 1, 0, 0 
        for cha in s:
            if flag == 0 :
                if cha == '-':
                    sign, flag = -1, 1
                    continue
                elif cha == ' ' : continue
                elif cha == '+' :
                    sign, flag = 1, 1
                    continue
            if cha.isdigit() : 
                flag = 1
                ret = ret*10+int(cha)
            else : break
        ret *= sign
        if -2**31 > ret:
            ret = -2**31
        elif ret >= 2**31 :
            ret = 2**31 -1
        return ret
        