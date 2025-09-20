class A:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a/self.b
    
class B(A):
    def __init__(self,a,b):
        super().__init__(a,b)

    def display(self):
        print(self.add())
        print(self.sub())
        print(self.mul())
        print(self.div())
        
abc =['apple','banana','orange']

def iteration():
    for i in abc:
        print(i)