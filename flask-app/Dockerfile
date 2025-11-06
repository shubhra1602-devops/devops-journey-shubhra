# Use official Python image as the base
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from your project to container's /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]