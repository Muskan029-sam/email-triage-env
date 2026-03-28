# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies (no cache to keep image small)
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run your environment
CMD ["python", "env.py"]
