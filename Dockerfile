
# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python application and picture
COPY hello.py .
COPY app/ ./app/

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["python", "hello.py"]
