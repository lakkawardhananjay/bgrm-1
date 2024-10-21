# Use an official Python 3.9 image as the base
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy all files to the working directory
COPY . .

# Expose port 5100
EXPOSE 5100

# Set the command to run the application
CMD ["python", "app.py"]
