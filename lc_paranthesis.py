# Correct Paranthesis

class stack(object):
    def __init__(self):
        self.top_st = []
        
    def push(self, element):
        self.top_st.insert(0, element)
        
    def pop(self):
        self.top_st.pop(0)
    
    def peek(self):
        return self.top_st[0]
 
        
def correct_paranthesis(st):
    
    d = {")":"(", "}":"{", "]":"["}
    l1 = ["(", "{", "["]
    
    paranthesis_st = stack()
    
    for i in st:
        if i in l1:
            paranthesis_st.push(i)
            #print(paranthesis_st.peek())
        else:
            #print(paranthesis_st.peek())
            if paranthesis_st.peek() == d[i]:
                paranthesis_st.pop()
            else:
                return False
    return True
    
print(correct_paranthesis("{[]}()"))