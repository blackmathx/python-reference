FROM python:3.11

# Set working directory
WORKDIR /app

# Install vim
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

# Install pandas (optional, remove if not needed)
RUN pip install numpy pandas matplotlib

# Start bash shell
CMD ["bash"]
