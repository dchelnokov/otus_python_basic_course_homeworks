FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /homework3_docker_container

RUN pip install --upgrade pip
RUN pip install "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --only main

COPY hw3 .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

EXPOSE 8000

# Comment to the OTUS Team:
# This container runs with  "docker run -p 8000:8000 -it hw3_docker_project" without quote marks!
# Dmitry Chelnokov 2023-06-14