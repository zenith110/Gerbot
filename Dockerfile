# set base image (host OS)
FROM python:3.7.9
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
# set the working directory in the container
WORKDIR /updater/

# copy the content of the local src directory to the working directory
COPY src/ .

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.7.9-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# command to run on container start
CMD [ "python", "./main.py" ]
