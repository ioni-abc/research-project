import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from fault_injections import service_unavailable
from utils import setup_logging, setup_observability

app = FastAPI(title="Database Service")
setup_observability(app, "database_service")

load_dotenv()
logger = setup_logging("database_service")

inventory = {"laptop": 5, "mouse": 10}


@app.post("/reserve/{item}")
async def reserve_item(item: str):
    logger.info("Post request for reserve - Database service")

    # Trigger Fault Injection - Service Unavailable RF12
    if os.getenv("INJECT_SERVICE_UNAVAILABLE") == "true":
        service_unavailable()

    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        return {"status": "reserved", "item": item, "remaining": inventory[item]}

    raise HTTPException(status_code=400, detail="Item out of stock or invalid")
