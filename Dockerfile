# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY calculator.py app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8081

# Run the web app
CMD ["python", "app.py"]