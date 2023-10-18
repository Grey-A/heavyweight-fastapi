from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.user.apis import router as user_router

app = FastAPI(title="Heavyweight(FastAPI)", docs_url="/")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(user_router, prefix="/user", tags=["user"])
