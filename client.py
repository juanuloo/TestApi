import requests

url = "http://127.0.0.1:3000"

def create_user(case_info):
    res = requests.post(f"{url}/add-case", json = case_info)

def view_user(userId):
    res = requests.get(f"{url}/user-data/{userId}")

if __name__ == "__main__":
    case_info = {
        "userId": "185046353",
        "description": "Speeding",
        "action": "Arrest order"
    }
    
    create_user(case_info)