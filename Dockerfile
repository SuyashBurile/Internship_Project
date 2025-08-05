# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Streamlit uses port 7860 by default
EXPOSE 7860

# Command to run the Streamlit app
CMD ["streamlit", "run", "obesity.py", "--server.port=7860", "--server.address=0.0.0.0"]
