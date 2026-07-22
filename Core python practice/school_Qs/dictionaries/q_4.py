m = {1: 54, 2: 89.9, 3: 74, 4: 73, 5: 65}
found = False

for i in m:
    if m[i] == 89.9:
        print(f"Roll number {i}hasscored 89.9")
        found = True

if not found:
    print("No one has scored 89.9")