from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

user_data = {}

@app.get("/user-data/<userId>")
def get_user(userId):
    data = user_data.get(userId)
    
    if not data:
        return jsonify({"error": "User couldn't be found"}), 404
    
    return jsonify({userId: data})

@app.post("/add-case")
def add_case():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"})

    userId = data.get("userId")
    
    if not userId:
        return jsonify({"error": "User id not found"})

    if userId in user_data:
        return jsonify({"error": "User already exists"})

    user_data[userId] = {
        "description": data.get("description"),
        "action": data.get("action")
        }
    
    return jsonify({"message": "User added", "userId": user_data[userId]}), 201

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000)