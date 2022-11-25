FROM python:3.10-slim

WORKDIR /code
COPY home_work26_docker/requirements.txt .
RUN pip install -r requirements.txt
COPY home_work26_docker/app.py .
COPY migrations migrations
COPY home_work26_docker/docker_config.py default_config.py

CMD flask run -h 0.0.0.0 -p 80
