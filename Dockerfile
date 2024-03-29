# Use an official Python runtime as a parent image
FROM python:3.10

# Define build arguments
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION

# Copy the current directory contents into the container 
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir awscli

# Set environment variables using build arguments
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_REGION=$AWS_REGION

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PORT=80

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

