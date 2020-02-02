class Base:
    def __init__(self,r=0,i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

ob = Base(2,3)
ob.getData()

ob2 = Base(5)
ob2.attr = 10
print(ob2.real,ob2.imag,ob2.attr)