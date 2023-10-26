from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI

from app.logging import MyLogger

logging.basicConfig(level=logging.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger = MyLogger.getLogger(__file__)
    logger.info("############# app start!")
    yield
    logger.info("############# app shudown")


app = FastAPI(lifespan=lifespan)
