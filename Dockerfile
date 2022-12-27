FROM python:3.9.7

# Set the working directory
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirement.txt .
RUN pip install -r requirement.txt

# Copy the rest of the project files
COPY . .

# Expose the default Django port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]