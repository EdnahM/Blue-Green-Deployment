FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create templates directory if it doesn't exist
RUN mkdir -p templates
# Move HTML template to templates directory
RUN mv index.html templates/ 2>/dev/null || true

# Security: Run as non-root user
RUN useradd -m appuser
USER appuser

# Default environment variable
ENV APP_VERSION=blue
ENV PORT=8080

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
