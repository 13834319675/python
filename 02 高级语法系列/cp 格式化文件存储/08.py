import json

data = {"name":"chenpeng","age":18}

with open("t.json","w") as f:
    json.dump(data,f)


with open("t.json","r") as f:
    d = json.load(f)
    print(d)