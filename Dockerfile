FROM python:3.11-slim

ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"
ENV PYTHONPATH="/fids_resonator"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /app

# RUN apt-get install -y procps

ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

EXPOSE 8009

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8009", "--log-level", "debug",  "--reload"]