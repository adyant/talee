'''
Created on Jul 27, 2016

@author: adyant
'''
class ListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def get_Data(self):
        return str(self.data)
    
    def get_next(self):
        return self.next
    
    def set_next(self,new_next):
        self.next = new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            n = ListNode(data)
            self.head = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            newnode = ListNode(data)
            n.next = newnode
    
    def printll(self):
        n = self.head
        while n:
            print n.data      
            n = n.next


    def reverse(self,start):
        curr = start
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


if __name__ == '__main__':
    mylist = LinkedList()
    elements = [1,2,3,4,5]
    for elem in elements:
        mylist.append(elem)
    
    mylist.head = mylist.reverse(mylist.head)
    mylist.printll()