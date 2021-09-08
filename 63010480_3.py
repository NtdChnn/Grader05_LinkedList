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

    def __str__(self):
        s = ''
        p = self.head
        while p is not None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def indexOf(self, data):
        q = self.head
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

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

    def listOfData(self):
        lod = []
        p = self.head
        while p is not None:
            lod.append(str(p.data))
            p = p.next
        lod.reverse()
        return lod


ipl1, ipl2 = input('Enter Input (L1,L2) : ').split(' ')
ipl1 = str(ipl1)
ipl2 = str(ipl2)
ipl1 = [e for e in ipl1.split('->')]
ipl2 = [e for e in ipl2.split('->')]

l1 = SinglyLinkedListNoDummy()
l2 = SinglyLinkedListNoDummy()

for i in ipl1:
    l1.append(i)
for i in ipl2:
    l2.append(i)
print('L1    : ',end='')
print(l1)
print('L2    : ',end='')
print(l2)

listL2 = l2.listOfData()
for i in listL2:
    l1.append(i)
print('Merge : ',end='')
print(l1)