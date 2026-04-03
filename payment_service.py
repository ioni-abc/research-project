import os

from dotenv import load_dotenv
from fastapi import FastAPI

from fault_injections import long_response_time
from utils import setup_logging, setup_observability

app = FastAPI(title="Payment Service")
setup_observability(app, "payment_service")

load_dotenv()
logger = setup_logging("payment_service")


@app.post("/pay")
async def process_payment():
    logger.info("Post request for pay - Payment service")

    # Trigger Fault Injection - Long Response Time PF20
    if os.getenv("LONG_RESPONSE_TIME") == "true":
        await long_response_time()

    return {"status": "paid"}
