FROM python:3.11.4

WORKDIR /app

RUN pip install --no-cache-dir pipenv
COPY . ./
RUN pipenv install --system --deploy --ignore-pipfile