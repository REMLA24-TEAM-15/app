#Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root
EXPOSE 8080
CMD ["poetry", "run", "python3", "src/main.py"]
