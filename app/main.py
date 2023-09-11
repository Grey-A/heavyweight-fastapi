from fastapi import FastAPI

from app.user.apis import router as user_router

app = FastAPI(title="Heavyweight(FastAPI)", docs_url="/")


# Routers
app.include_router(user_router, prefix="/user", tags=["user"])
