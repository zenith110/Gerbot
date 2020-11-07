# set base image (host OS)
FROM python:3.7-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# set the working directory in the container
WORKDIR /updater/

# copy the content of the local src directory to the working directory
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

FROM python:3.7-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
CMD [ "python", "./main.py" ]
