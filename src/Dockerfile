FROM python:3.10 AS builder

WORKDIR /src

RUN python -m venv /opt/venv
ENV PATH='/opt/venv/bin:${PATH}'

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN pip install uvicorn

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
