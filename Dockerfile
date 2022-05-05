# Container image that runs your code
FROM python:3.9-alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
RUN mkdir /.oblivious
COPY .oblivious/service.yaml /.oblivious/service.yaml

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
