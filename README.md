# fastAPI-experimental

A test of both fastAPI and toolforge's build pack service

Initialized following the steps in https://wikitech.wikimedia.org/wiki/Help:Toolforge/My_first_Python_ASGI_tool

Built using python 3.10.12

## Running locally

`uvicorn app:app --reload` to start the local server


## Deployment to Toolforge

1. `pip freeze > requirements.txt` to set dependencies (remember to run this every time I add a new dependency)
2. create a Procfile (see the tutorial for guidelines)
3. `ssh` into Toolforge, `become` the tool in question, `toolforge build start <repo url>`
4. wait for `toolforge build show` to return `ok(Succeeded)`
5. start the webservice with `toolforge webservice buildservice start --mount=none`

### Deployment troubleshooting
1. `toolforge build logs` will display the last build logs
2. `toolforge webservice --backend kubernetes buildservice logs` might reveal some information, in a case where the build passed, but the webservice does not work