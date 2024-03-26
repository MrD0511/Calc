class Eval():
    def __init__(self,str):
        self.str=str    
    def f(self,ch):
        f={}
        f['+']=1
        f['-']=1
        f['*']=f['/']=3
        f['^']=6
        f['(']=9
        f[')']=0
        if ch in f:
            return f[ch]
        else:
            return 7
    def g(self,ch):
        g={}
        g['+']=g['-']=2
        g['*']=g['/']=4
        g['^']=5
        g['(']=0
        g[')']=0
        if ch in g:
            return g[ch]
        else:
            return 8
    def in2post(self,str):
        str=str+')'
        st=[]
        st.append('(')
        indx=0
        curr=str[indx]
        output=[]
        mid=""
        while(curr):
            if(self.f(curr)!=7 and len(mid)!=0):
                st.append(mid) 
                mid=""
            while self.f(curr) < self.g(st[-1]):
                output.append(st.pop())
            if self.f(curr) == 7:
                mid=mid+curr
            else:
                if(curr==')'):
                    st.pop()
                else:
                    st.append(curr)
            indx+=1
            if indx>len(str)-1:
                break
            curr=str[indx]
        return output
    def evaluate(self):
        input=self.in2post(self.str)
        indx=0
        curr=input[indx]
        st=[]
        try:
            while(curr):
                if self.f(curr)==7:
                    st.append(curr)
                else:
                    val2=float(st.pop())
                    val1=float(st.pop())
                    if(curr=='+'):
                        st.append(val1+val2)
                    elif curr=='-':
                        st.append(val1-val2)
                    elif curr=='*':
                        st.append(val1*val2)
                    elif curr=='/':
                        st.append(val1/val2)
                    elif curr=='^':
                        st.append(val1**val2)
                indx+=1
                if indx>=len(input):
                    break
                curr=input[indx]
        except:
            return "Math Error"
        return st.pop()

eval=Eval("1+2+")
print(eval.evaluate())