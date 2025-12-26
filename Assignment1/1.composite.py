items=[]

def add_items(payload=None):
    if not payload or not isinstance(payload, dict):
        return "no data yet"
    items.append(payload)
    return "data is added"


def get_items():
    if not items:
        return "no item"
    return {"item":items}

def search_items(key, value):
    results = [i for i in items if i.get(key) == value]
    return results if results else "No matching items found"

def handle(request ,payload=None):
    #  method, path = request.split(maxsplit=1)
    method, path, payload = request.get("method"), request.get("endpoint"), request.get("data")

    try:
        if method=="GET" and path=="/items":
            return get_items()
        
        elif method=="POST" and path=="/items":
            return add_items(payload)
        
        elif method == "GET" and path.startswith("/items?"):
            query = path.split("?", 1)[1]   
            key, value = query.split("=", 1)
            return filter_items(key, value)
        
        else:
            return "invalid path"
        
    except Exception as e:
        return {f"error",{str(e)}}


# print(handle({"POST /items"},"{"method":"GET","endpoint":"/items","data":{"id":101}}"))
print(handle({"method":"POST","endpoint":"/items","data":{"id":101}}))
print(handle({"method":"GET","endpoint":"/items"}))
