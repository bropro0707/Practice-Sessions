import json
with open("JASON_contact_book.json","r") as f:
    data = json.load(f)
n_data = json.dumps(data,indent=5)
print(n_data)
