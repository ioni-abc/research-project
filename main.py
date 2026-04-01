import httpx
import time

AUTH_URL = "http://localhost:8001/login"
ORDER_URL = "http://localhost:8002/checkout"

def run():
    print("Start")
    with httpx.Client() as client:
        try:
            print("log in")
            response = client.post(AUTH_URL, json={"username": "admin", "password": "admin"})
            token = response.json().get("token")

            headers = {"Authorization": f"Bearer {token}"}
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == "__main__": 
    run()
    # uvicorn.run("auth_service:app", host="127.0.0.1", port=8001, reload=True)