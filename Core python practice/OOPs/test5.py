class NodeList:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    
node1 = NodeList()
node2 = NodeList()
node3 = NodeList()

node1.next = node2
node2.next = node3

head = node1
current = head
count = 0
def count(head):
    current = head
    count = 0
    if current.val is None:
        print("Empty")
    while current is not None:
        count += 1
        current = current.next
    print(count)
count(head)