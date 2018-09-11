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
    def findposition(self, string1):
        string =self.posi(string1)
        if self.ware[int(string[0])][int(string[1:3])].get(string)==None:
            print(self.ware[int(string[0])][int(string[1:3])])
            return True
        else:
            return False
    def checksort(self,list):
        k=[]
        for i in list:
            a = self.string2code(i)
            b = str(int(a) + 101000)
            k.append(self.findposition(b))
        if False in k:
            return False
        else:
            return True
    def sort(self,x,y):
        u=[]
        for i in self.ware[x-1][y-1]:
            if bool(self.code(self.ware[x-1][y-1][i],self.rownum[x-1])==i)==False:
                c= self.ware[x-1][y-1][i]
                u.append(c)
        if self.checksort(u)==True:
            for i in u:
                a = self.string2code(i)
                b=str(int(a)+101000)
                self.retrieve(i)
                self.insert(i,b)
                return True
        else:
            return False
    def find(self,string):
        r = int((ord(string[0]) % 65) / 5)
        b = int(string[1])
        if self.row[b - 1][r].get(string)!=None:
            return True
        else:
            return False

    def checkWare(self, x):
        list = []
        for i in self.ware[x-1]:
            # print(i)
            if i != {}:
                list.append(i)
        print(len(list)+1)
        if len(list) >= self.num[0]:
            print("Slot is empty. Cannot retrieve the product. ")
        else:
            print("Slot is not empty. ")

w = warehouse()
w.insert("A111","519099")
w.insert("A181","519098")
w.insert("A121","515099")
w.insert("A171","502099")
w.checkWare(5)
# print(w.ware5)
