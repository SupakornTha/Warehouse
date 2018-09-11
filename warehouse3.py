class warehouse:
    def __init__(self):
        self.row1 = [{},{},{},{},{}]
        self.row2 = [{},{},{},{},{}]
        self.row3 = [{},{},{},{},{}]
        self.row4 = [{},{},{},{},{}]
        self.row5 = [{},{},{},{},{}]
        self.ware1 = [{},{},{},{},{}]
        self.ware2 = [{},{},{},{},{}]
        self.ware3 = [{},{},{},{},{}]
        self.ware4 = [{},{},{},{},{},{},{}]
        self.ware5 = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
        self.row=[self.row1,self.row2,self.row3,self.row4,self.row5]
        self.num=[500,500,500,175,8000]
        self.rownum=[5,5,5,7,20]
        self.slotnum=[100,100,100,25,400]
        self.posit=[65,70,75,80,85]
        self.ware = [self.ware1,self.ware2,self.ware3,self.ware4,self.ware5]
        self.belt  = []
    def code(self, string,row):
        a = str(((ord(string[0]) % 65) / 5))
        b = str((ord(string[0])+(int(string[1:])-1)%self.slotnum[int(a)]))
        c = int(a) + int(string[1]) + int(string[2]) + int(string[3])
        d = str((c % row))
        if len(d) == 1:
            d = "0" + d
        if len(b)==2:
            b="0"+b
        return (a+str(d)+str(b))
    def posi(self,string):
        a=str(int(string[0])-1)
        if len(string[1:])==3:
            return a + "0"+str(int(string[1])-1)+"0"+string[2:]
        elif len(string[1:])==5:
            b=str(int(string[1:3])-1)
            if len(b)==1:
                b="0"+ b
            return a+b+string[3:]
    def string2code(self,string):
        c = int(self.code(string, 20)[0])
        d = self.rownum[c]
        product=self.code(string,d)
        return product
    def insert(self,data1,position1):
        a=int((ord(data1[0]) % 65) / 5)
        b=int(data1[1])-1
        position=self.posi(position1)
        if  (self.row[b][a].get(data1)==None)and (self.ware[int(position[0])][int(position[1:3])].get(position)==None):
            self.row[b][a][data1]=position
            self.ware[int(position[0])][int(position[1:3])][position]=data1
    def retrieve(self,string):
        r=int((ord(string[0]) % 65) / 5)
        b=int(string[1])
        a=self.row[b-1][r]
        c = a.get(string)
        a.pop(string)
        self.ware[int(c[0])][int(c[1:3])].pop(c)
        print(int(c)+101000)
    def sort(self,x,y):
        u=[]
        for i in self.ware[x-1][y-1]:
            if bool(self.code(self.ware[x-1][y-1][i],self.rownum[x-1])==i)==False:
                c= self.ware[x-1][y-1][i]
                u.append(c)
        for i in u:
            self.retrieve(i)
            a=self.string2code(i)
            c=str(int(a[1:3])+1)
            if len(c)==1:
                c="0"+c
            b=str(int(a[0])+1)+c+a[3:]
            self.insert(i,b)

    def find(self, string):
        r = int((ord(string[0]) % 65) / 5)
        b = int(string[1])
        if self.row[b - 1][r].get(string) != None:
            return True
        else:
            return False

w = warehouse()
w.insert("A111","519099")
