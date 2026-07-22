w = {}
n = int(input("How many winners are there: "))
for key in range(0,n):
    N = str(input("Enter the name of the winner: "))
    n_w = int(input("Enter the number of wins: "))
    w[N] = n_w
print(w)