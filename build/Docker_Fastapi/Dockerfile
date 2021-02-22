FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./build/Docker_Fastapi/requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /code

COPY ./config ./config

COPY ./core ./core

