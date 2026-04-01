from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

import os

load_dotenv()

app = FastAPI(title="Warehouse Service")

inventory = {
    "laptop": 5,
    "mouse": 10
}

@app.post("/reserve/{item}")
async def reserve_item(item: str):
    # Fault Injection RF12 - Service Unavailable
    print("-----")
    print(os.getenv("INJECT_RF12"))
    print("-----")
    if os.getenv("INJECT_RF12") == "true":
        print(f"CRASH TRIGGERED: Cannot reach database for {item}")
        raise HTTPException(status_code=500, detail="Database Connection Lost")
    
    # Expected behaviour
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        print(f"Reserved 1 {item}. Remaining: {inventory[item]}")
        return {"status": "reserved", "item": item, "remaining": inventory[item]}
    
    # If item doesn't exist or is out of stock
    raise HTTPException(status_code=400, detail="Item out of stock or invalid")