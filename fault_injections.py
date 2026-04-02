from dotenv import load_dotenv
from fastapi import HTTPException
from utils import setup_logging
import asyncio

load_dotenv()
logger = setup_logging("fault injections")

def cpu_hog():
    """
    PF31: A fault injection that causes CPU Hog, by running a heavy computation.
    """
    logger.info("PF31: INJECTED CPU HOG FAULT")
    count = 0
    for i in range(2 * 10**7):
        count += i

def service_unavailable():
    """
    RF12: A fault injection that causes the database connection to be lost.
    """
    logger.info("RF12: INJECTED SERVICE UNAVAILABLE FAULT")
    raise HTTPException(status_code=500, detail="Database Connection Lost")

async def long_response_time():
    """
    PF20: A fault injection that causes Long Response Time.
    """
    logger.info("PF20: INJECTED LONG RESPONSE TIME FAULT")
    await asyncio.sleep(8)
