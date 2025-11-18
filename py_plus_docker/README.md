PYTHON-DOCKER PROJECT USAGE

# Build the image (do this once, or when CSV changes)
docker build -t pydocker-env .

# Run container with your project folder mounted (--rm flag auto-deletes the container on exit)
# Linux 
docker run -it --rm -v $(pwd):/app pydocker-env
# Windows
docker run -it --rm -v "%cd%:/app" pydocker-env


# Now you're inside. Your folder is mounted at app/
# Changes made to your files will be reflected in the container

# Exit (container auto-deletes)
exit
