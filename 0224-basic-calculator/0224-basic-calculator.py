from collections import defaultdict

class Solution:
    def list2num(self,n_list:list) -> int:
        ret = 0
        for i in range(len(n_list)-1,-1,-1):
            ret = ret*10 + int(n_list[i])
        return ret

    def read_num(self,s_list:list,cha:str)->int:
        s_list.append(cha)
        ret = []
        while s_list :
            temp = s_list[-1]
            if not temp.isdigit():
                ans = self.list2num(ret)
                if temp == '-':
                    ans *= -1
                    s_list.pop()
                return s_list,ans 
            else :
                ret.append(temp)
                s_list.pop()
        else : return s_list, self.list2num(ret)
    
    def calculate(self, s: str) -> int:
        s_list, ret = list(s) , 0
        term_dict = defaultdict(list) 
        not_calculated, depth = [], 0
        while s_list :
            cha = s_list.pop()
            if cha == ')' : depth += 1 
            elif cha == '(' :
                term_dict[depth-1].append(term_dict[depth][-1])
                del term_dict[depth]
                depth -= 1
            elif cha == '-' :
                term_dict[depth][-1] *= -1
                s_list.append('+')
                continue
            elif cha == '+' :
                continue
            elif cha == ' ' : continue
            else :
                s_list, num = self.read_num(s_list,cha)
                term_dict[depth].append(num)
                if len(term_dict[depth]) > 1 :
                    term_dict[depth] = [sum(term_dict[depth])]
        
        return sum(term_dict[0])
