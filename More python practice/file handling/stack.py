def isempty(stk):
    if stk == []:
        True
    else:
        False

def push(stk,item):
    stk.append(item)
    top = len(stk)-1

def pop(stk):
    if isempty:
        print("Stack is underflow")
    else:
        stk.pop()
        if stk==[]:
            top = None
        else:
            top = len(stk)-1

def printitem(stk):
    if isempty(stk):
        print("Stack have no item")
    else:
        top = len(stk)-1
        for i in range(top,-1,-1):
            print(stk[i])

def peek(stk):
    if isempty(stk):
        print("Stack have no item")
    else:
        top = len(stk)-1
        print(f"Top most item is{top}")

# __main__
stack= []
top = None
while True:
    print("OPERATIONS")
    print('''1.Push
2.pop
3.display
4.peek
5.break''')
    choice = int(input("Enter your choice: "))
    if choice==1:
        i = int(input("add no. you want to push: "))
        push(stack,i)
    elif choice==2:
        pop(stack)
    elif choice==3:
        printitem(stack)
    elif choice==4:
        peek(stack)
    elif choice == 5:
        break
    