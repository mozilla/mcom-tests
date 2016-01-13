FROM debian:jessie

WORKDIR /app
CMD ["./run.sh"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends python2.7 libpython2.7 build-essential python-dev python-pip && \
    rm -rf /var/lib/apt/lists/*

ENV BASE_URL "https://www-dev.allizom.org"
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt pytest-xdist

COPY . /app
