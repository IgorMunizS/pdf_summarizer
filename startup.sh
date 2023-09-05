#!/bin/sh
env $(cat .env) uvicorn app.__main__:app --host ${API_HOST} --port ${API_PORT} &
env $(cat .env) python -m app.gradio_app