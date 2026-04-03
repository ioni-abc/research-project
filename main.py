import httpx
import time
import os
from utils import setup_logging
from dotenv import load_dotenv

load_dotenv()
logger = setup_logging("main")

AUTH_URL = os.getenv("AUTH_URL")
ORDER_URL = os.getenv("ORDER_URL")

def run():
    logger.info("Starting order simulation")
    with httpx.Client() as client:
        try:
            
            # Log in simulation
            auth_response = client.post(AUTH_URL, json={"username": "admin", "password": "admin"})
            token = auth_response.json().get("token")
            headers = {"Authorization": f"Bearer {token}"}

            start_time = time.time()

            # Placing order simulation
            order_response = client.post(ORDER_URL, json={"item": "laptop"}, headers=headers)
            logger.info(order_response.json())
            end_time = time.time()
            
            logger.info(f"Total Time: {end_time - start_time:.2f} seconds")
            
        except Exception as e:
            logger.error(f"Something happened: {e}")

if __name__ == "__main__": 
    run()