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
        if len(self) == 0:
            return 'List is empty'
        else :
            s = 'link list : '
            p = self.head
            while p != None:
                s += str(p.data)
                p = p.next
                if p != None:
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


ip = [i for i in input("Enter Input : ").split(',')]

ll = SinglyLinkedListNoDummy()
count = 0
for i in ip:
    if count != 0:
        index, data = i.split(':')
        index = int(index)
        if len(ll) < index or index < 0:
            print("Data cannot be added")
            print(ll)
        else :
                ll.insertAfter(index-1,data)
                print(f'index = {index} and data = {data}')
                print(ll)
    else:
        if len(i) != 0:
            j = i.split(" ")
            for k in j:
                ll.append(k)
        print(ll)
        count += 1

