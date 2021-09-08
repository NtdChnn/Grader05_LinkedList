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
        self.isLoop = False

    def __str__(self):
        if len(self) == 0:
            return 'Empty'
        else :
            s = ''
            p = self.head
            while p is not None:
                s += str(p.data)
                p = p.next
                if p is not None:
                    s+= '->'
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
        if self.head is None:
            self.head = self.Node(data, None)
            self.size += 1
        else:
            self.insertAfter(self.size - 1, data) #len(self) = จำนวนสมาชิก - 1 คือ index

    def insertAfter(self,i,data) :      #มีสายข้อมูลอยู่แล้ว
        i = int(i)
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
        i = int(i)
        if self.size > 0:
            p = self.nodeAt(i)
            p.next = p.next.next
            self.size -= 1

    def delete(self,i) :
        i = int(i)
        if i == 0 and self.size > 0 :             #  ลบตัวแรก
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)  #  ลบตัวก่อนหน้า

    def set_next(self, id1, id2):
        id1 = int(id1)
        id2 = int(id2)
        if len(self) == 0:
            print('Error! {list is empty}')
        elif id1 >= len(self):
            print('Error! {index not in length}: '+ str(id1))
        elif id2 >= len(self):
            print(f'index not in length, append : {id2}')
            self.append(id2)
        else:
            print('Set node.next complete!, index:value = ',end='')
            p = self.nodeAt(id1)
            q = self.nodeAt(id2)
            print(f'{id1}:{str(p.data)} -> {id2}:{str(q.data)}')
            if id2 <= id1:
                self.isLoop = True
            else:
                p.next = q
                self.size -= (id2 - id1) - 1

    def checkLoop(self):
        if self.isLoop:
            print('Found Loop')
        else:
            print('No Loop')
            print(self)

ip = [e for e in input("Enter input : ").split(',')]

l1 = SinglyLinkedListNoDummy()

for i in ip:
    command, Data = i.split(' ')
    Data = str(Data)
    if command == 'A':
        l1.append(Data)
        print(l1)
    else:
        ID1, ID2 = Data.split(':')
        l1.set_next(ID1,ID2)

l1.checkLoop()
