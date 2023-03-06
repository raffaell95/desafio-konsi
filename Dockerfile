FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./.env /app/.env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

RUN pytest

CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "80"]