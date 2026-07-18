class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def insert_head(head,val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

def insert_end(head,val):
    new_node = ListNode(val)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def deletion(head,val):
    if head is not None and head.val == val:
        return head.next
    current = head
    while current is not None and current.next is not None:
        if current.next.val == val:
            current.next == current.next.next
            return head
    return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

head = node1

#operations
head = insert_head(head,0)
head = insert_end(head,4)
head = deletion(head,0)
#print func
current = head
while current is not None:
    print(current.val,end="-")
    current = current.next
print(None)