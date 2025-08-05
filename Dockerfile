# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 7860

# Command to run the Streamlit app
CMD ["streamlit", "run", "src/obesity.py", "--server.port=7860", "--server.address=0.0.0.0"]
