FROM python:3.12-slim

WORKDIR /app

# Нужно для readiness (curl) и для Allure CLI (Java)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip default-jre \
 && rm -rf /var/lib/apt/lists/*

# Allure CLI
ENV ALLURE_VERSION=2.29.0
RUN curl -fsSL -o /tmp/allure.tgz \
    https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz \
 && tar -xzf /tmp/allure.tgz -C /opt \
 && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
 && rm /tmp/allure.tgz

# Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Project code + tests
COPY . /app

# По умолчанию, но в CI мы обычно переопределяем команду
CMD ["pytest", "-q"]
