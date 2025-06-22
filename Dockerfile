FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all contents from your local App/ folder into the container
COPY App/ ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will use
EXPOSE 80

# Run the app
CMD ["python", "app.py"]

