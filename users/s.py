import json


def original():
    with open("./fixtures/userinit.json") as o:
        data = json.load(o)
    return data


def regular():
    with open("./dump.json") as n:
        data = json.load(n)
    return [d for d in data if d["model"] == "users.user"]


# with open('./userinit.json') as p:
r = regular()
o = original()

for u in r:
    for user in o:
        if user["fields"]["username"] == u["fields"]["username"]:
            user["fields"]["password"] = u["fields"]["password"]
json_object = json.dumps(o, indent=4)
print(json_object)
with open("./fixtures/userinit.json", "w") as outfile:
    outfile.write(json_object)
