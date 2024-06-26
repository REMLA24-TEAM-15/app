#Dockerfile
FROM python:3.10.14
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root
COPY . /app
EXPOSE 8080
CMD ["poetry", "run", "python3", "src/main.py"]
