# Start with the official Python image
FROM python:3.9-slim

# Set a directory for the app
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
