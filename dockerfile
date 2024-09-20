# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Install TruffleHog
RUN pip install truffleHog

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Give execution rights to the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/app/entrypoint.sh"]
