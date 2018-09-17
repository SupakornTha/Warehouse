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
        a = str(int((ord(string[0]) % 65) / 5))
        b = str((int((ord(string[0]))+(int(string[1:])-1))%int(self.slotnum[int(a)])))
        c = int(a) + int(string[1]) + int(string[2]) + int(string[3])
        d = str((c % row))
        if len(d) == 1:
            d = "0" + d
        if len(b)==2:
            b="0"+ b
        elif len(b) ==1:
            b="00"+b
        return (a+str(d)+str(b))
    def posi(self,string):
        a=str(int(string[0]))
        if len(string[1:])==3:
            return a + "0"+str(int(string[1]))+"0"+string[2:]
        elif len(string[1:])==5:
            b=str(int(string[1:3]))
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
        if self.ware[int(string[0])][int(string[1:3])].get(string)!=None:
            return False
        else:
            return True
    def checksort(self,list):
        k=[]
        for i in list:
            a = self.string2code(i)
            b = str(int(a))
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
                self.retrieve(i)
                self.insert(i,a)
        else:
            return False
    def find(self,string):
        r = int((ord(string[0]) % 65) / 5)
        b = int(string[1])
        if self.row[b - 1][r].get(string)!=None:
            return True
        else:
            return False

    def checkname(self,string):
        if 1<=int(string[1])<=5:
            if 0<=int(string[2:])<=99:
                if 97<=ord(string[0])<=121:
                    return chr(ord(string[0])-32)+string[1:]
                elif 65<=ord(string[0])<=89:
                    return string
        else:
            return False
    def checkRow(self, x):
        x=x-1
        for i in range(self.rownum[x]):
            if self.ware[x][i] >= self.slotnum[x]:
                print("Slot is empty. Cannot retrieve the product. ")
    def checknumber_product(self,w):
        t=0
        for i in self.ware[w-1]:
            t+=len(i)
        return t
    def get_item(self,ware,row):
        w=""
        for i in self.ware[ware][row]:
            w+= str(self.ware[ware][row].get(i))+","

        return w[:len(w) - 1]
    def findproduct(self, string):
        r = int((ord(string[0]) % 65) / 5)
        b = int(string[1])
        return self.row[b - 1][r].get(string)


    def info(self):
        print (" 0XXXX:Retrieve a product id XXXX")
        print (" 1XXXX:Store a product id XXXX")
        print (" 2XY00:Sort warehouse X at row Y")
        print (" 30000:Retrieve a product from the conveyor belt")
        print (" 40000:Output information of all warehouses")
        print (" 5XXXX:Search for a product ID XXXX")
        print (" 9XXXXYYYY Manually put a product id XXXX at position YYYY ")
        print (" Product id has a unique id in a form of 4 characters: XYZ")
        print ("  X  has a value of A to Y.")
        print ("  Y has a value of 1 to 5.")
        print ("  Z has a value of 00 to 99.")
        print (" To enter the position please enter 6 digit number ABC")
        print ("  A  represents a number of warehouse.It has a value of 1 to 5.")
        print ("  B  represents a number of row in warehouse.It has a value of 01 to 20.")
        print ("  C  represents a number of slot.It has a value of 001 to 400.")
    def data(self):
        for i in range(len(self.ware)):
            print ("Warehouse "+str(i+1))
            print ("Numbers of Rows: "+str(self.rownum[i]))
            print ("Numbers of total products:"+str(self.checknumber_product(i+1)))
            for j in range(self.rownum[i]):
                if self.get_item(i,j)=="":
                    b="-"
                else:
                    b=self.get_item(i,j)
                print ("Product in row "+str(j+1)+": id "+b)

    def command(self):
        print("")
        a = input("Please Enter the Command:")
        # print(len(a))
        if 4<len(a)<7:
            if a[0] == "0" and len(a)==5 and (65<=ord(a[1])<=89 or 97<=ord(a[1])<=121) and 49<=ord(a[2])<=53 and 48<=ord(a[3])<=57 and 48<=ord(a[4])<=57 :
                if self.checkname(a[1:]) == False or len(a) != 5: #or self.find(a[2:]) == True:
                    print ("Invalid product id. Please check the product id again")
                    return self.command()
                else:
                    b = self.checkname(a[1:])
                    if self.find(b) == False:
                        print ("Slot is empty. Cannot retrieve the product.")
                        return self.command()
                    elif self.belt == 10:
                        print ("Belt is full. Cannot retrieve the product ")
                        return self.command()
                    else:
                        c = self.findproduct(b)
                        self.retrieve(b)
                        self.belt.append(b)
                        # print(c)
                        print ("-Moving from Belt to Warehouse 1")
                        if int(c[0]) == 2:
                            print ("-Moving from Warehouse 1 to Warehouse 3")
                        elif int(c[0]) == 1 or int(c[0]) > 2:
                            print ("-Moving from Warehouse 1 to Warehouse 2")
                            if int(c[0]) > 2:
                                print("-Moving from Warehouse 2 to Warehouse " + str(int(c[0]) + 1))
                        print ("-Getting a product id " + b + " from Warehouse" + str(int(c[0]) + 1) + " : row " + str(int(c[1:3]) + 1) + " slot " + str(int(c[3:])))
                        if int(c[0]) > 2:
                            print ("-Moving from Warehouse " + str(int(c[0]) + 1) + " to Warehouse 2")
                        if int(c[0]) == 1 or int(c[0]) > 2:
                            print ("-Moving from Warehouse 2 to Warehouse 1")
                        elif int(c[0]) == 2:
                            print ("-Moving from Warehouse 3 to Warehouse 1")
                        print ("-Moving from Warehouse 1 to Belt")
                        print ("-Place product id "+b+" on the belt")
                        print ("-Retrieving Successfully! ")
                        return self.command()

            elif a[0] == "1" and len(a)==5 and (65<=ord(a[1])<=89 or 97<=ord(a[1])<=121) and 49<=ord(a[2])<=53 and 48<=ord(a[3])<=57 and 48<=ord(a[4])<=57:
                if self.checkname(a[1:]) == False or len(a) != 5:
                    print ("Invalid product id. Please check the product id again")
                    return self.command()
                else:
                    b = self.checkname(a[1:])
                    c = self.string2code(b)
                    # print(b,c)
                    if self.findposition(c) == False:
                        print ("Slot is occupied. Cannot store the product.")
                        return self.command()
                    else:
                        if len(self.ware[int(c[0])][int(c[1:3])])<self.slotnum[int(c[0])]:
                            self.insert(b, c)
                            print ("-Moving from Belt to Warehouse 1")
                            if int(c[0])==2:
                                print ("-Moving from Warehouse 1 to Warehouse 3")
                            elif int(c[0])==1 or int(c[0])>2:
                                print ("-Moving from Warehouse 1 to Warehouse 2")
                                if int(c[0])>2:
                                    print("-Moving from Warehouse 2 to Warehouse "+str(int(c[0])+1))
                            print ("-Storing a product id " + b + " from Warehouse"+ str(int(c[0])+1)+" : row " + str(int(c[1:3])+1) + " slot " + str(int(c[3:])))
                            if int(c[0]) > 2:
                                print("-Moving from Warehouse "+ str(int(c[0])+1)+" to Warehouse 2")
                            if int(c[0])==1 or int(c[0])>2:
                                print("-Moving from Warehouse 2 to Warehouse 1")
                            elif int(c[0])==2:
                                print("-Moving from Warehouse 3 to Warehouse 1")
                            print("-Moving from Warehouse 1 to Belt")
                            print("-Storing Successfully!")
                        else:
                            print("Slot is occupied. Cannot store the product.")
                        return self.command()
            elif a[0] == "2" and len(a)==5 and a[len(a)-2:]=="00" and 49<=ord(a[1])<=53 :
                if int(a[1]) not in range(0, 6) or int(a[2:len(a) - 2]) > self.rownum[int(a[1]) - 1]:
                    print("Invalid command.The command must include 2XY00 while X is a warehouse number and Y is a row number")
                    return self.command()
                else:
                    b = a[1:len(a) - 2]
                    if self.sort(int(b[0]), int(b[1:])) == False:
                        print ("Slot is occupied. Cannot sort Warehouse " + b[0] + " Row " + b[1:])
                        return self.command()
                    else:
                        self.sort(int(b[0]), int(b[1:]))
                        print ("Sorting process for Warehouse " + b[0] + " is complete.")
                        return self.command()
            elif a == "30000":
                if len(self.belt) == 0:
                    print ("The belt is empty. Cannot retrieve the product from the belt")
                    return self.command()
                else:
                    b = self.belt.pop(0)
                    c = len(self.belt)
                    print ("Retrieve a product with id " + b + " from the belt. ")
                    if c <= 1:
                        print ("The belt now has " + str(c) + " product on the line")
                    else:
                        print ("The belt now has " + str(c) + " products on the line")
                    return self.command()
            elif a=="40000":
                self.data()
                return self.command()
            elif a[0] == "5" and len(a)==5  and (65<=ord(a[1])<=89 or 97<=ord(a[1])<=121) and 49<=ord(a[2])<=53 and 48<=ord(a[3])<=57 and 48<=ord(a[4])<=57:
                if 65<=ord(a[1])<=89 or 97<=ord(a[1])<=121:
                    if self.checkname(a[1:])!=False:
                        b = self.checkname(a[1:])
                        if self.find(b)==False:
                            print ("Product not found.")
                            return self.command()
                        else:
                            c=w.findproduct(b)
                            print("Found the product at Warehouse: "+str(int(c[0])+1)+" row: "+str(int(c[1:3])+1)+" slot: "+str(int(c[3:])))
                            print(self.command())
                else:
                    print ("Invalid command.")
                    return self.command()
            else:
                print ("Invalid command.")
                return self.command()
        elif len(a)==11:
            # print("c")
            if a[0] == "9"  and (65<=ord(a[1])<=89 or 97<=ord(a[1])<=121) and 49<=ord(a[2])<=53 and 48<=ord(a[3])<=57 and 48<=ord(a[4])<=57:
                if a[5] == "0":
                    print("Invalid command.")
                    return self.command()
                elif self.checkname(a[1:5])==False:
                    print ("Invalid command.")
                    print (" 9XXXXYYYY Manually put a product id XXXX at position YYYY ")
                    print (" Product id has a unique id in a form of 4 characters: XYZ")
                    print ("  X  has a value of A to Y.")
                    print ("  Y has a value of 1 to 5.")
                    print ("  Z has a value of 00 to 99.")
                    print (" To enter the position please enter 6 digit number ABC")
                    print ("  A  represents a number of warehouse.It has a value of 1 to 5.")
                    print ("  B  represents a number of row in warehouse.It has a value of 01 to 20.")
                    print ("  C  represents a number of slot.It has a value of 001 to 400.")
                    return self.command()
                else:
                    b=self.checkname(a[1:5])
                    d=self.posi(a[5:])
                    e=str(int(d[1:3])-1)
                    if len(e)==1:
                        e="0"+e
                    c=str(int(int(d[0])-1))+e+d[3:]
                    #print(c)
                    if self.find(b)==False:
                        print ("Product not found.")
                        return self.command()
                    else:
                        if self.findposition(c)==False:
                            print ("Slot is occupied. Failed to move.")
                            return self.command()
                        else:
                            # print(b)
                            # print(c)
                            self.retrieve(b)
                            self.insert(b,c)
                        print ("Move product "+b+" to Warehouse: "+str(int(d[0]))+" row: "+str(int(d[1:3]))+" slot: "+str(int(d[3:])))
                        return self.command()

        else:
            print("Invalid command.")
            return self.command()

w = warehouse()
w.info()
w.command()