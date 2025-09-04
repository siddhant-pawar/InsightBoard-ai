FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Poetry
COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry

# Install dependencies via Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Optional: install additional dependencies from req.txt
COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt || true

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI app with Uvicorn
CMD ["sh", "-c", "python migrate.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
