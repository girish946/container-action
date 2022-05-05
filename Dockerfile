# Container image that runs your code
FROM python:3.9-alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
RUN mkdir /.oblivious
COPY .oblivious/service.yaml /.oblivious/service.yaml

# Create a virtualenv and install python dependencies
RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install  checksumdir==1.0.5 PyYAML requests Flask


# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
