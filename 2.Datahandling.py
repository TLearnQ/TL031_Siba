import json

def case(data):
    if not data or isinstance(data,dict):
        return {k.lower(): case(v) for k, v in data.items()}
    if not data or isinstance(data,list):
        return [case(i) for i in data]
    
    return data

example={"config":{"Site":"Bangalore","Devices":12}}

cleaned=case(example)
items = [example["config"]]
group={}
for i in items:
    site=i["Site"]
    if site not in group:
        group[site]=[]
    group[site].append(i)

with open(f"hello.json","w") as f:
     json.dumps(cleaned , indent=4)




print(cleaned)


