# Use an official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /App

# Copy app code
COPY App/ ./app/
COPY App/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80
EXPOSE 80

# Run the app
CMD ["python", "App/app.py"]
