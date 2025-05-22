# Use the latest official Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port and run
EXPOSE 8080
CMD ["python", "app.py"]
