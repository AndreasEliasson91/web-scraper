FROM python:3.10 AS builder

WORKDIR /src

RUN python -m venv /opt/venv
ENV PATH='/opt/venv/bin:${PATH}'

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src/

EXPOSE 8080

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
