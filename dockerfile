FROM ubuntu:latest # Base image for our container

RUN apt-get update && apt-get install -y poetry # Update and install nginx

# Set working directory (optional)
# WORKDIR /var/www/html

# Copy your application code (replace with your copy command)
# COPY . .  # This copies everything from the current directory to the container

# Expose the port (adjust if your application uses a different port)
# EXPOSE 80

# Start command (replace with your application's start command)
# CMD ["nginx", "-g", "daemon off;"]
