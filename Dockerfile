FROM python:2

WORKDIR /app

ENV BASE_URL "https://www-dev.allizom.org"
ENV BROWSER_NAME Firefox
ENV BROWSER_VERSION 39.0
ENV PLATFORM "Windows 7"
ENV SELENIUM_VERSION 2.47.1
ENV SAUCE_CREDENTIALS_PATH /tmp/creds
ENV BUILD_TAG docker

ENV PYTHONDONTWRITEBYTECODE=1
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt pytest-xdist

COPY . /app

CMD ["./run.sh"]
