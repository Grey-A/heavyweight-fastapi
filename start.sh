#!/bin/sh
set -e

PORT=${PORT:-8000}

alembic upgrade head

uvicorn app.main:app --host "0.0.0.0" --port 8000