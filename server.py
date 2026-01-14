from contextlib import asynccontextmanager

from fastapi import FastAPI, Response

from app.core.config import settings
from app.core.routers import controller_list
from app.utils.log_utils import logger


# 生命周期事件
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("应用启动中...")
    yield
    logger.info("应用关闭中...")


app = FastAPI(
    title=settings.app_name,
    description=f"{settings.app_name} 接口文档",
    version=settings.app_version,
    lifespan=lifespan,
)


@app.get("/health")
def health_check(response: Response):
    response.status_code = 200
    return {"status": "ok!"}


# 注册路由
for controller in controller_list:
    app.include_router(router=controller.get("router"), tags=controller.get("tags"), prefix=controller.get("prefix"))
