Complex=type("Complex",(object,),{"__init__": lambda self,r,i: (lambda _:setattr(self,"r",r))(setattr(self,"i",i)), "__add__": lambda self,no:Complex(self.r+no.r,self.i+no.i),"__sub__": lambda self,no:Complex(self.r-no.r,self.i-no.i),"__mul__": lambda self,no:Complex(self.r*no.r-self.i*no.i,self.r*no.i+self.i*no.r),"__truediv__":lambda self,no:(lambda mod: (lambda _:(lambda fin: (lambda _:fin)([setattr(fin,"r",fin.r/mod),setattr(fin,"i",fin.i/mod)]))(self*no))(setattr(no,"i",-no.i)))(no.mod().r **2),"mod":lambda self:Complex((self.r**2+self.i**2)**(0.5),0),"__str__":lambda self:"%.2f+0.00i" % (self.r) if self.i == 0 else ("0.00+%.2fi" % (self.i) if self.i >= 0 else "0.00-%.2fi" % (abs(self.i))) if self.r == 0 else ("%.2f+%.2fi" % (self.r, self.i)) if self.i > 0 else "%.2f-%.2fi" % (self.r, abs(self.i))})

# Can't remove, boilerplate code
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')