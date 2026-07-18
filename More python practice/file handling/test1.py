def isempty(stk):
    if stk == []:
        True
    else:
        False
def push(stk):
    a = int(input("Enter the item to add: "))
    stk.append(a)
    top = len(stk)-1
def pop(stk):
    if isempty:
        print("stack is underflow")
    else:
        stk.pop()
        if stk == []:
            top = None
        else:
            top = len(stk)-1
def showitem(stk):
    if isempty:
        print("stack is empty")
    else:
        for i in range(len(stk)-1,-1,-1):
            print(i)
def peek(stk):
    if isempty:
        print("Stack is empty")
    else:
        top = len(stk)-1
        print(top)
#__main__
stack = []
top = None
while True:
    print("1.Push")
    print("2.Pop")
    print("3.showitem")
    print("4.Peek")
    print("5.Break")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        push(stack)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        showitem(stack)
    elif choice == 4:
        peek(stack)
    elif choice == 5:
        break
    