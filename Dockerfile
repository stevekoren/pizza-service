# Use a smaller base image
FROM python:3.11-slim as builder

ENV WORKDIR /app
WORKDIR ${WORKDIR}

# Copy just the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Build the final image
FROM python:3.11-slim as final

ENV WORKDIR /app
WORKDIR ${WORKDIR}

# Copy application code from the builder stage
COPY --from=builder ${WORKDIR} ${WORKDIR}

# Create a non-root user
RUN groupadd -g 1001 appuser && useradd -r -u 1001 -g appuser appuser

# Change ownership of the application directory
RUN chown -R appuser:appuser ${WORKDIR}

USER appuser

EXPOSE 8080

# Define a HEALTHCHECK
HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
