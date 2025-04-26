import requests

# access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmciLCJpZCI6NSwicm9sZSI6InVzZXIiLCJleHAiOjE3NDU1MzQ2NDN9.54Gmb5K7SgW6Nqs6QBbckVJybg8cuwHdguBEUJK8PDs"

def call_api_post(access_token, payload):
    """
    Makes a POST request to the given URL with Bearer token and JSON payload.

    Args:
        url (str): API endpoint URL
        access_token (str): Bearer token for authorization
        payload (dict): Data to send in the request body

    Returns:
        dict or str: JSON response or error text
    """
    url = "http://127.0.0.1:8000/todos/todo/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    

    try:
        response = requests.post(url, headers=headers, json=payload)

        # Raise exception for bad HTTP status codes
        response.raise_for_status()

        return { "result": "Created: Todo...","details":payload }
    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)
        return str(e)

def call_api_put(access_token, payload):
    """
    Makes a POST request to the given URL with Bearer token and JSON payload.

    Args:
        url (str): API endpoint URL
        access_token (str): Bearer token for authorization
        payload (dict): Data to send in the request body

    Returns:
        dict or str: JSON response or error text
    """

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    title = payload["title"]
    url = f"http://127.0.0.1:8000/todos/{title}"
    

    response = requests.get(url, headers=headers)

    id = response.json()["id"]
    for key,value in payload.items():
        if value == None:
            payload[key]=response.json()[key]
    
    try:
        url = f"http://127.0.0.1:8000/todos/{id}"
        response = requests.put(url, headers=headers, json=payload)

        # Raise exception for bad HTTP status codes
        response.raise_for_status()

        return { "result": "Updated: Todo...","details":payload }
    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)
        return str(e)

def call_api_delete(access_token, payload):
    """
    Makes a POST request to the given URL with Bearer token and JSON payload.

    Args:
        url (str): API endpoint URL
        access_token (str): Bearer token for authorization
        payload (dict): Data to send in the request body

    Returns:
        dict or str: JSON response or error text
    """

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    title = payload["title"]
    url = f"http://127.0.0.1:8000/todos/{title}"
    
    response = requests.get(url, headers=headers)

    id = response.json()["id"]
    for key,value in payload.items():
        if value == None:
            payload[key]=response.json()[key]
    
    try:
        url = f"http://127.0.0.1:8000/todos/{id}"
        response = requests.delete(url, headers=headers)

        # Raise exception for bad HTTP status codes
        response.raise_for_status()

        return { "result": "Deleted: Todo...","details":payload }
    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)
        return str(e)