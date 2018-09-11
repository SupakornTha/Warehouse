class warehouse:
    def __init__(self):
        self.ware  = [None]*9675
        self.ware1 = [None]*500
        self.ware2 = [None]*500
        self.ware3 = [None]*175
        self.ware4 = [None]*8000
        self.ware5 = {}
        self.belt = []

    def arrange(self,string):
        a=str(ord(string[0])%65)+string[2:]+str(int(string[1])-1)
        return (int(a))
    def doubleHashing(self,data1,data2,warehouse, hashTableSize, doubleHashSize):
        data=self.arrange(data1)
        primaryHash = data % hashTableSize
        doubleHash = primaryHash
        if warehouse[primaryHash] is None:
            warehouse[primaryHash] = {data2:data1}
        else:
            while warehouse[doubleHash] is not None:
                secondary = doubleHashSize - (data % doubleHashSize)
                doubleHash = (doubleHash + secondary) % hashTableSize
            warehouse[doubleHash] = {data2:data1}

    def command(self,b):
        if b[0]=="1":
            if b[1:] not in self.ware:
                if  ord(b[1]) < 71:
                    print("-Moving from Belt to Warehouse 1")
                    print("-Storing a product id " + b[1:] + " from Warehouse 1: row " + b[2] + " slot " + b[3:])
                    print("-Moving from Warehouse1 to Start")
                    print("-Place product id " + b[1:] + " on the belt")
                    print("-Storing Successfully!")
                    print("")
                    self.doubleHashing(b[1:],b[1:],self.ware1,500,500)
                    self.doubleHashing(b[1:],b[1:],self.ware,9675,9675)
                """elif  len(self.ware2)<=500 and b[1] in "FGHIJ":
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Storing a product id " + b[1:] + " from Warehouse 2: row " + b[2] + " slot " + b[3:]
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Storing Successfully!"
                    print""
                    self.ware2[b[1:]]=b[1:]
                    self.ware[b[1:]] = b[1:]
                elif  len(self.ware3)<=500 and b[1] in "KLMNO":
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 3"
                    print "-Storing a product id " + b[1:] + " from Warehouse 3: row " + b[2] + " slot " + b[3:]
                    print "-Moving from Warehouse3 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Storing Successfully!"
                    print""
                    self.ware3[b[1:]]=b[1:]
                    self.ware[b[1:]] = b[1:]
                elif  len(self.ware4)<=175 and b[1] in "PQRST":
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 4"
                    print "-Storing a product id " + b[1:] + " from Warehouse 4: row " + b[2] + " slot " + b[3:]
                    print "-Moving from Warehouse4 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Storing Successfully!"
                    print""
                    self.ware4[b[1:]]=b[1:]
                    self.ware[b[1:]] = b[1:]
                elif  len(self.ware5)<=8000 and b[1] in "ABCDEFGHIJKLMNOPQRSTUVWXY":
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 4"
                    print "-Storing a product id " + b[1:] + " from Warehouse 5: row " + b[2] + " slot " + b[3:]
                    print "-Moving from Warehouse4 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Storing Successfully!"
                    print""
                    self.ware5[b[1:]]=b[1:]
                    self.ware[b[1:]] = b[1:]
            else:
                print "Slot is occupied. Cannot store the product."
                print""
        if b[0]=="0":
            a=self.call(b[1:])
            if a==None:
                print "Slot is empty. Cannot retrieve the product."
                print""
            elif len(self.belt)>=10:
                print "Belt is full. Cannot retrieve the product "
                print""
            else:
                if a in self.ware1:
                    print "-Moving from Belt to Warehouse 1"
                    print "-Getting a product id "+b[1:]+" from Warehouse 1: row " + a[1]+ " slot "+a[2:]
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id "+b[1:]+" on the belt"
                    print "-Retrieving Successfully!"
                    print""
                    self.belt.append(a)
                    self.ware1.pop(b[1:],None)
                    self.ware.pop(b[1:], None)
                elif a in self.ware2:
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Getting a product id "+b[1:]+" from Warehouse 2: row " + a[1]+ " slot "+a[2:]
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id "+b[1:]+" on the belt"
                    print "-Retrieving Successfully!"
                    print""
                    self.belt.append(a)
                    self.ware2.pop(b[1:],None)
                    self.ware.pop(b[1:],None)
                elif a in self.ware3:
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 3"
                    print "-Getting a product id " + b[1:] + " from Warehouse 3: row " + a[1] + " slot " + a[2:]
                    print "-Moving from Warehouse3 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Retrieving Successfully!"
                    print""
                    self.belt.append(a)
                    self.ware3.pop(b[1:], None)
                    self.ware.pop(b[1:], None)
                elif a in self.ware4:
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 4"
                    print "-Getting a product id " + b[1:] + " from Warehouse 4: row " + a[1] + " slot " + a[2:]
                    print "-Moving from Warehouse4 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Retrieving Successfully!"
                    print""
                    self.belt.append(a)
                    self.ware4.pop(b[1:], None)
                    self.ware.pop(b[1:], None)
                elif a in self.ware5:
                    print "-Moving from Belt to Warehouse 1"
                    print "-Moving from Warehouse1 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 5"
                    print "-Getting a product id " + b[1:] + " from Warehouse 5: row " + a[1] + " slot " + a[2:]
                    print "-Moving from Warehouse5 to Warehouse 2"
                    print "-Moving from Warehouse2 to Warehouse 1"
                    print "-Moving from Warehouse1 to Start"
                    print "-Place product id " + b[1:] + " on the belt"
                    print "-Retrieving Successfully!"
                    print""
                    self.belt.append(a)
                    self.ware5.pop(b[1:], None)
                    self.ware.pop(b[1:], None)
        if b[0] == "9":
            if b[5:8] in self.ware:
                print ("Slot is occupied. Failed to move")
            else:
                self.ware[b[1:4]]=b[5:8]
                if len(self.ware1)<=500 and b[1] in "ABCDE":
                    self.ware1[b[5:8]]=b[1:4]
                elif len(self.ware2) <= 500 and b[1] in "FGHIJ":
                    self.ware2[b[5:8]]=b[1:4]
                elif len(self.ware3) <= 500 and b[1] in "KLMNO":
                    self.ware3[b[5:8]]=b[1:4]
                elif len(self.ware4) <= 175 and b[1] in "PQRST":
                    self.ware4[b[5:8]]=b[1:4]
                elif len(self.ware5) <= 8000 and b[1] in "ABCDEFGHIJKLMNOPQRSTUVWXY":
                    self.ware5[b[5:8]]=b[1:4]
                print ("Move product "+ b[1:4]+ " to " +b[5:8])"""








w=warehouse()
w.command("1A120")
w.command("1A101")

w.command("1A120")
w.command("1A101")
w.command("1A101")
w.command("1F101")
print (w.ware1)
#w.command("0A101")
#w.ware["A101"]="A109"
#w.ware1["A101"]="A109"
#w.command("0A109")
#w.command("0Y120")
#w.command("9Y")"""