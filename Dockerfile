# set base image (host OS)
FROM python:3.7.9-slim

# set the working directory in the container
WORKDIR /updater/

# copy the content of the local src directory to the working directory
COPY src/ .



# command to run on container start
CMD [ "python", "./main.py" ]
