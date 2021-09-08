class SinglyLinkedListNoDummy:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.head = None
        self.size = 0
        self.beforeRiffle = []
        self.count = []

    def __str__(self):
        if len(self) == 0:
            return 'List is empty'
        else :
            s = ''
            p = self.head
            while p != None:
                s += str(p.data)
                p = p.next
                if p != None:
                    s+= ' '
            return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.head
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):  # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def append(self, data):
        if self.head == None:
            self.head = self.Node(data, None)
            self.size += 1
        else:
            self.insertAfter(self.size - 1, data) #len(self) = จำนวนสมาชิก - 1 คือ index

    def insertAfter(self,i,data) :      #มีสายข้อมูลอยู่แล้ว
        if i == -1:
            p = self.Node(data)
            p.next = self.head
            self.head = p
        else:
            q = self.nodeAt(i)
            p = self.Node(data)
            p.next = q.next
            q.next = p
        # q.next = self.Node(data,q.next)
        self.size += 1

    def deleteAfter(self, i):  # มีสายข้อมูลอยู่แล้ว
        if self.size > 0:
            p = self.nodeAt(i)
            p.next = p.next.next
            self.size -= 1

    def delete(self,i) :
        if i == 0 and self.size > 0 :             #ลบตัวแรก
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)  #ลบตัวก่อนหน้า

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data) - 1)

    def BottomUp(self, index):
        index -= 1
        a = self.nodeAt(len(self) - 1)
        b = self.nodeAt(index+1)
        c = self.nodeAt(index)
        a.next = self.head
        self.head = b
        c.next = None

    def DeBottomUp(self, index):
        index *= -1
        index += len(self)
        a = self.nodeAt(len(self) - 1)
        b = self.nodeAt(index)
        c = self.nodeAt(index - 1)
        a.next = self.head
        self.head = b
        c.next = None

    def Riffle(self, index):
        L1 = []
        L2 = []
        count = 0
        p = self.head
        while p != None:
            self.beforeRiffle.append(str(p.data))
            if len(self.beforeRiffle) > index:
                L2.append(p.data)
            else: L1.append(p.data)
            p = p.next
        if len(L1) >= len(L2):
            count += 1
            for i in L2:
                L1.insert(count, i)
                count += 2
            self.count = L1
        else:
            for i in L1:
                L2.insert(count, i)
                count += 2
            self.count = L2

    def showRiffle(self):
        print(*self.count,sep=' ')
        self.count = []

    def showDeRiffle(self):
        print(*self.beforeRiffle,sep=' ')
        self.beforeRiffle = []


ipll, ipcm = input('Enter Input : ').split('/')
ipll = str(ipll)
ipll = ipll.split(' ')
ipcm = str(ipcm)
ipcm = ipcm.split('|')

l1 = SinglyLinkedListNoDummy()
for i in ipll:
    l1.append(i)

for i in ipcm:
    print('--------------------------------------------------')
    print('Start : ', end='')
    print(l1)
    if i[:1] == 'B':
        B, R = i.split(',')
    else:
        R, B = i.split(',')
    B = str(B)
    R = str(R)
    b, bper = B.split(' ')
    r, rper = R.split(' ')
    bper = float(bper)
    rper = float(rper)
    bIn = int((bper / 100) * len(l1))
    rIn = int((rper / 100) * len(l1))
    bper = "{:.3f}".format(bper)
    rper = "{:.3f}".format(rper)
    l1.BottomUp(bIn)
    print(f'BottomUp {bper} % : ',end='')
    print(l1)
    l1.Riffle(rIn)
    print(f'Riffle {rper} % : ',end='')
    l1.showRiffle()
    print(f'Deriffle {rper} % : ', end='')
    l1.showDeRiffle()
    l1.DeBottomUp(bIn)
    print(f'Debottomup {bper} % : ', end='')
    print(l1)
print('--------------------------------------------------')
