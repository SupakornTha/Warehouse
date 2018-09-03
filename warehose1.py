class warehouse:
    def __init__(self):
        self.ware={}
    def warehouse1(self):
        t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(0, 25):
            for j in range(1, 6):
                for l in range(0, 4):
                    # print(self.ware)
                    self.ware[str(t[i]) + str(j) + "0" + str(l)] = ""

    def command(self,b):
        if b[0]=="1":
            self.ware[b[1:]]=b[1:]
    def call(self,a):
        for i in self.ware:
            if i[0]==a[0]:
                print(i)
w=warehouse()
w.warehouse1()
# w.ware["B101"]="ware"
# w.call("A101")
# w.command("1A101")
print(w.ware)