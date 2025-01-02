import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000/items"
AUTH = HTTPBasicAuth("admin", "password123")

def get_items():
    response = requests.get(BASE_URL, auth=AUTH)
    if response.status_code == 200:
        print("Catalog:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.json()}")

def add_item(item):
    response = requests.post(BASE_URL, json=item, auth=AUTH)
    if response.status_code == 201:
        print("Item added successfully.")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

def get_item(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}", auth=AUTH)
    if response.status_code == 200:
        print(f"Item {item_id}:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.json()}")

def update_item(item_id, updates):
    response = requests.put(f"{BASE_URL}/{item_id}", json=updates, auth=AUTH)
    if response.status_code == 200:
        print("Item updated successfully.")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}", auth=AUTH)
    if response.status_code == 200:
        print("Item deleted successfully.")
    else:
        print(f"Error: {response.status_code}, {response.json()}")

# Example usage:
if __name__ == "__main__":
    # Get all items
    get_items()

    # Add a new item
    new_item = {"id": 2, "price": 150, "size": "L", "color": "blue"}
    add_item(new_item)

    # Get a specific item
    get_item(2)

    # Update an item
    update_item(2, {"price": 200, "color": "green"})

    # Delete an item
    delete_item(2)

    # Get all items again
    get_items()
