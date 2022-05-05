# container-action
Docker container action

This is a trial project for Github docker container action.

The project executes on every `push` on `main` branch.
It checks for a file `.oblivious/service.yaml`.
Which holds a (dummy) schema for authorized users along with their roles.

- The workflow starts an `python:3.9-alpine` container.
- Checks if `.oblivious/service.yaml` exists.
- Checks if `.oblivious/service.yaml` contains a valid schema.
- If yes, executes a python script that takes a `username` as an argument and checks it with the schema.
  If it exists in the schema, then it communicates it to a remote server.
  