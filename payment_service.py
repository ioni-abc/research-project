from fastapi import FastAPI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv
app = FastAPI(title="Payment Service")

@app.post("/pay")
async def process_payment():
    # Fault Injection PF20 - Latency
    if os.getenv("INJECT_LATENCY"):
        print("latency pf20 injected")
        await asyncio.sleep(8)
    
    print("successful process payment")
    return {"status": "paid"}

