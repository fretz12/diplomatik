# Diplomatik Prod Build

## Building a Docker Image

To build the docker image, build it from the root directory and point to the Dockerfile in this directory. Specifically,
the build command is:

`docker build -f deployment/docker/prod/Dockerfile --tag diplomatik:<IMAGE_VERSION> .`

## Sample Docker Compose

Also provided is a sample docker compose file on how to run the container. There are a few ways to pass in the 
application environment variables:

1. The .env file can be passed in directly and referred to in the compose file. This is specified in the sample.
2. The env vars can be define in the compose file
3. The env vars can be defined on the command line if directly running the container without the compose file
4. 