FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl unzip default-jre \
 && rm -rf /var/lib/apt/lists/*

ENV ALLURE_VERSION=2.29.0
RUN curl -fsSL -o /tmp/allure.tgz \
    https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz \
 && tar -xzf /tmp/allure.tgz -C /opt \
 && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
 && rm /tmp/allure.tgz

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["pytest", "-q"]
