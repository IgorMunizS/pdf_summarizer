#!/bin/sh
env $(cat .env) python -m src.data_ingestion
env $(cat .env) uvicorn app.__main__:app --host ${API_HOST} --port ${API_PORT} &
env $(cat .env) gradio app/gradio_app.py