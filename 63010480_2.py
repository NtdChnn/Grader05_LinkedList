class DoublyLinkedListNoDummy:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data

            if prev is None:
                self.prev = None
            else:
                self.prev = prev

            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if len(self) != 0:
            s = ''
            p = self.head
            for i in range(len(self)):
                s += str(p.data) + ' '
                p = p.next
            return s
        else: return 'Empty'


    def reverse(self):
        s = 'Linked List Reverse : '
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)):
            s += str(p.data) + ' '
            p = p.prev
        print(s,end='')
        if len(self) == 0:
            print('Empty')

    def __len__(self):
        return self.size

    def show(self):
        print('Linked List : ',end='')
        print(self)

    def Size(self):
        print(f'Linked List size = {len(self)} : ',end='')
        print(self)

    def isEmpty(self):
        return self.size == 0

    def index(self, data):
        q = self.head
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def Index(self, data):
        q = self.head
        ID = self.index(data)
        print(f'Index ({data}) = {ID} : ',end='')
        print(self)

    def isIn(self, data):
        return self.index(data) >= 0

    def search(self, data):
        if self.index(data) >= 0:
            print(f"Found {data} in ",end='')
        else:
            print(f"Not Found {data} in ",end='')
        print(self)

    def nodeAt(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def append(self, data):
        if self.head == None:
            self.head = self.Node(data)
        else:
            q = self.nodeAt(len(self) - 1)
            x = self.Node(data, q, None)
            q.next = x
        self.size += 1

    def addHead(self, data):
        if self.head == None:
            self.head = self.Node(data)
        else:
            p = self.Node(data)
            p.next = self.head
            self.head.prev = p
            self.head = p
        self.size += 1

    def removeNode(self, q):
        p = q.prev
        x = q.next
        p.next = x
        x.prev = p
        self.size -= 1

    def pop(self, i):
        i = int(i)
        if i >= len(self) or i < 0 or len(self) == 0:
            print('Out of Range | ',end='')
            print(self)
        else:
            print('Success | ',end='')
            print(self,end='')
            if i == 0:
                if len(self) == 1:
                    self.head = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                self.size -= 1
            elif i == len(self) - 1:
                x = self.nodeAt(i)
                p = x.prev
                p.next = None
                self.size -= 1
            else:
                self.removeNode(self.nodeAt(i))
            print('-> ',end='')
            print(self)


    def insert(self, i, data):
        i = int(i)
        if i == 0 or i <= -1*len(self):
            self.addHead(data)
        elif len(self) > i > -1*len(self):
            if i < 0:
                i += len(self)
            q = self.nodeAt(i - 1)
            o = self.nodeAt(i)
            p = self.Node(data)
            p.next = q.next
            q.next = p
            p.prev = q
            o.prev = p
            self.size += 1
        elif i >= len(self):
            self.append(data)

ip = [e for e in input('Enter Input : ').split(',')]

l2 = DoublyLinkedListNoDummy()

for i in ip:
    if i[:2] == 'AP':
        command, data = i.split(' ')
        l2.append(data)
    elif i[:2] == 'AH':
        command, data = i.split(' ')
        l2.addHead(data)
    elif i[:2] == 'SE':
        command, data = i.split(' ')
        l2.search(data)
    elif i[:2] == 'ID':
        command, data = i.split(' ')
        l2.Index(data)
    elif i[:2] == 'SI':
        l2.Size()
    elif i[:2] == 'PO':
        command, Index = i.split(' ')
        l2.pop(Index)
    elif i[:2] == 'IS':
        command, Index, data = i.split(' ')
        l2.insert(Index,data)

l2.show()
l2.reverse()
