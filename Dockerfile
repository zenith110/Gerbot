# set base image (host OS)
FROM python:3.10-slim


# set the working directory in the container
WORKDIR /updater/

# copy the content of the local src directory to the working directory
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./main.py" ]
