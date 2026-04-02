from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
from utils import setup_logging
from fault_injections import cpu_hog
import os
import httpx

app = FastAPI(title="Order Service")

load_dotenv()
logger = setup_logging("order_service")

DB_URL = os.getenv("DB_URL")
PAYMENT_URL = os.getenv("PAYMENT_URL")

class OrderRequest(BaseModel):
    item: str


@app.post("/checkout")
async def checkout(order: OrderRequest, authorization:str = Header(None)):
    logger.info("Post request for checkout - Order service")

    if authorization != "Bearer valid_token_12345":
        raise HTTPException(status_code=401, detail="Invalid or missing Token")
    
    # Trigger Fault Injection - CPU Hog PF31
    if os.getenv("INJECT_CPU_HOG") == "true":
        cpu_hog()

    async with httpx.AsyncClient() as client:
        try:

            # Call database service
            db_respone = await client.post(f"{DB_URL}/{order.item}")
            if db_respone.status_code != 200:
                raise HTTPException(status_code=db_respone.status_code, detail=db_respone.json())

            # Call payment service
            pay_response = await client.post(PAYMENT_URL)
            if pay_response.status_code != 200:
                raise HTTPException(status_code=500, detail="Payment failed")
                
            return {"order_status": "completed", "item": order.item}
            
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Network error: {e}")