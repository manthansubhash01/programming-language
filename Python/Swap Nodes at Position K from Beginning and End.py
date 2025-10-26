'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
'''
def swapNodes(head, k):
    temp = head 
    while temp.next is not None:
        temp = temp.next
    tail = temp
    start = head
    end = tail
    while k > 1:
        start = start.next
        end = end.prev
        k -= 1
    start.data, end.data = end.data, start.data