from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies import get_db
from app.example_module.apis import router as example_router

app = FastAPI(
    title="Heavyweight(FastAPI)",
    docs_url="/",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}, # Hides Schemas Menu in DocsF
)

# Variables
origins = ["*"]

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health Check
@app.get("/health", status_code=200, include_in_schema=False)
def health_check(db=Depends(get_db)):
    """This is the health check endpoint"""
    return {"status": "ok"}


# Routers
app.include_router(example_router, prefix="/example", tags=["Example Docs"])
