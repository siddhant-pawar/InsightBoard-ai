FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && poetry install --no-root
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
