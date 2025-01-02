from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

# Store user credentials (username: password)
users = {
    "admin": "password123",
    "user": "userpass"
}

# Store catalog data
data_file = "catalog.json"

# Load initial catalog data or create an empty file
def load_catalog():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save catalog data
def save_catalog(catalog):
    with open(data_file, "w") as file:
        json.dump(catalog, file, indent=4)

catalog = load_catalog()

# Authenticate users
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


# Routes
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the catalog API!'}), 200


# API endpoints
@app.route("/items", methods=["GET", "POST"])
@auth.login_required
def manage_items():
    if request.method == "GET":
        return jsonify(catalog)

    elif request.method == "POST":
        item = request.json
        if not all(key in item for key in ["id", "price", "size"]):
            return jsonify({"error": "Missing required fields."}), 400

        item_id = str(item["id"])
        if item_id in catalog:
            return jsonify({"error": "Item already exists."}), 400

        catalog[item_id] = {
            "price": item["price"],
            "size": item["size"],
            "color": item.get("color", "unknown")
        }
        save_catalog(catalog)
        return jsonify({"message": "Item added successfully."}), 201

@app.route("/items/<id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def manage_item(id):
    item_id = str(id)

    if request.method == "GET":
        if item_id not in catalog:
            return jsonify({"error": "Item not found."}), 404
        return jsonify(catalog[item_id])

    elif request.method == "PUT":
        if item_id not in catalog:
            return jsonify({"error": "Item not found."}), 404

        updates = request.json
        catalog[item_id].update(updates)
        save_catalog(catalog)
        return jsonify({"message": "Item updated successfully."})

    elif request.method == "DELETE":
        if item_id not in catalog:
            return jsonify({"error": "Item not found."}), 404

        del catalog[item_id]
        save_catalog(catalog)
        return jsonify({"message": "Item deleted successfully."})

if __name__ == "__main__":
    app.run(debug=True)
