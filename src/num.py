import math

class NUM:
    '''
    Summarizes a stream of numbers
    '''

    def __init__(self,at,txt) -> None:
        self.n=0
        self.mu=0
        self.m2=0
        self.lo=math.inf
        self.hi=-math.inf

        if(at):
            self.at = at
        else:
            self.at=0

        if(txt):
            self.txt = txt
        else:
            self.txt= ""

        if(self.txt[-1]=='-'):
            self.w=-1
        else:
            self.w=1


    def add(self,n) -> None:
        '''
        Add 'n', update lo,hi and stuff needed for standard deviation
        '''
        if(n!='?'):
            self.n=self.n+1
            d=n-self.mu
            self.mu=self.mu+d/self.n
            self.m2=self.m2+d*(n-self.mu)
            self.lo= min(n,self.lo)
            self.hi= max(n,self.hi)
        

    def mid(self,x) -> float:
        '''
        Return mean
        '''
        return self.mu

    def div(self,x) -> float:
        '''
        Return standard deviation using Welford's algorithm http://t.ly/nn_W
        '''
        if(self.m2<0 or self.n<2):
            return 0
        else:
            return (self.m2/(self.n-1))**0.5

    def rnd(self,x,n) -> float:
        if(x=='?'):
            return x
        else:
            self.rnd(x,n)
        