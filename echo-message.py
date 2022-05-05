#!/usr/bin/env python3
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from yaml import scanner

import os
import sys
import requests


def perform_request(user, data):
    headers = {"user-name": user}
    r = requests.post("http://localhost:5000/", headers=headers, json={"data": data})
    print(r.text)


def read_schema():
    """
    Reads the yaml file parses it and returns a dictionary containing the schema.
    """
    service_file = os.getenv("SERVICE_FILE")
    try:
        data_string = open(service_file).read()
        if data_string:
            schema = load(data_string, Loader=Loader)
            return schema
    except scanner.ScannerError as se:
        print(f"invalid schema {service_file}: {se}")
        sys.exit(1)


def validate_user(user, schema):
    """
    Validates the user based upon the schema and sends apt messate to the outside world.
    """
    if user in schema["users"]:
        print("user exists")
        branch = os.getenv("GH_BRANCH")
        actor = os.getenv("GH_ACTOR")
        hash_ = os.getenv("dir_hash")
        perform_request(user, f"Valid user: {user}:{actor}:{branch}:{hash_}")
    else:
        print(f"invalid user {user}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        schema = read_schema()
        # print(schema)
        validate_user(sys.argv[1], schema)
