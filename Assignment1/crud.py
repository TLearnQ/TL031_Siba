import requests
import json

url="https://jsonplaceholder.typicode.com/posts"

data={
    "name": "John Doe",
    "email": "jhon@gmail.com",
    "phone": "1234567890",
    "UserId": 1

}

response = requests.post(url, json=data)
print("\n Add data")
print(json.dumps(response.json(), indent=4))

get_response= requests.get(f"{url}/1")
print("\n Get data")
print(json.dumps(get_response.json(), indent=4))

update_data={
    "name": "Jane Doe",
    "email": "doe@gmail.com"
}
update_response = requests.put(f"{url}/1", json=update_data)
print("\n Update data")
print(json.dumps(update_response.json(), indent=4))

patch_data={
    "phone": "0987654321"
}
patch_response = requests.patch(f"{url}/1", json=patch_data)
print("\n Patch data")
print(json.dumps(patch_response.json(), indent=4))

delete_response = requests.delete(f"{url}/1")
print("\n Delete data")
print("Status Code:", delete_response.status_code)

# count the total endpoints
endpoints = {
    "POST /posts",
    "GET /posts/1",
    "PUT /posts/1",
    "PATCH /posts/1",
    "DELETE /posts/1"
}

unique_paths = {e.split(" ", 1)[1] for e in endpoints}

print("Total endpoints:", len(unique_paths))
