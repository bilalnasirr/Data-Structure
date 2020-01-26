class MNode:
    def __init__(self, value):
        self.value = value
        self.npx = {"Next":None,"Previous":None}

class MDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertatFirst(self, value):
        a = MNode(value)
        a.npx["Next"] = self.head
        a.npx["Previous"] = None
        if self.head == None:
            self.tail = a
        self.head = a

    def Print(self):
        a = self.head
        while a != None:
            print(a.value)
            a = a.npx["Next"]

    def InsertatEnd(self, value):
        x = MNode(value)
        if self.tail == None and self.head == None:
            self.tail = x
            self.head = x
        else:
            self.tail.npx["Next"] = x
            x.npx["Previous"] = self.tail
            self.tail = x

    def InsertAfter(self, s, item):
        a = MNode(item)
        x = self.head
        while x != None and x.value != s:
            x = x.npx["Next"]
        if x != None and x == self.tail:
            x.npx["Next"] = a
            a.npx["Previous"] = x
            self.tail = a
        elif x != None:
            a.npx["Next"] = x.npx["Next"]
            x.npx["Next"] = a
            a.npx["Previous"] = x
        else:
            self.InsertatEnd(item)

    def DeleteatFirst(self):
        if self.head == None:
            print('list is empty')
        else:
            self.head = self.head.npx["Next"]
            self.head.npx["Previous"] = None
            x = None

    def DeleteatEnd(self): 
        x = self.head
        while x.npx["Next"] != None:
            x = x.npx["Next"]
        self.tail = x.npx["Previous"]
        self.tail.npx["Next"] = None
        #x.npx["Previous"] = None
        #x.npx["Next"] = None

    def DeletebyValue(self, s):
        x = self.head
        if x.value == s:
            self.head = x.npx["Next"]
        else:
            while x.npx["Next"] != None and x.npx["Next"].value != s:
                x = x.npx["Next"]
            if x.npx["Next"].npx["Next"]== None:
                x.npx["Next"]=None
            else:
                x.npx["Next"] = x.npx["Next"].npx["Next"]
                x.npx["Next"].npx["Previous"] = x

    def InsertBefore(self, s, item):
        a = MNode(item)
        x = self.head
        if s == x.value:
            self.InsertatFirst(item)
        else:
            while x.npx["Next"] != None and x.npx["Next"].value != s:
                x = x.npx["Next"]
            a.npx["Next"] = x.npx["Next"]
            x.npx["Next"] = a
            a.npx["Previous"] = x

def Test():
    db=MDLinkedList()
    db.InsertatFirst(2)
    db.InsertatFirst(5)
    db.InsertatEnd(6)
    db.InsertBefore(5,7)
    db.InsertAfter(6,9)
    db.DeletebyValue(9)
    db.DeletebyValue(7)
    db.DeleteatEnd()
    db.DeleteatFirst()
    db.Print()

Test()