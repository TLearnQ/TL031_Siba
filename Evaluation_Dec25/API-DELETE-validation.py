

import requests
import json


import requests

def validate_delete_authorization():
    api_url = "https://httpbin.org/delete"
    token = "mytoken"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(api_url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

   
    auth = data.get("headers", {}).get("Authorization")

    if auth == f"Bearer {token}":
        return True
    else:
        return False


if __name__ == "__main__":
    result = validate_delete_authorization()
    print("Authorization Header Validation Result:", result)









#  headers ={
#     "Authorization": f"Bearer {TOKEN}",
#     "Accept": "application/vnd.github+json"
# }