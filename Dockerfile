FROM ubuntu:latest

RUN apt-get update && apt-get install -y poetry # Update and install nginx
RUN poetry install

# Set working directory (optional)
# WORKDIR /var/www/html

# Copy your application code
COPY catalogue catalogue
RUN main.py

# Expose the port (adjust if your application uses a different port)
# EXPOSE 80

# Start command (replace with your application's start command)
# CMD ["nginx", "-g", "daemon off;"]
