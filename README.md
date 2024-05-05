# fastAPI-experimental

A test of both fastAPI and toolforge's build pack service

Initialized following the steps in https://wikitech.wikimedia.org/wiki/Help:Toolforge/My_first_Python_ASGI_tool

Built using python 3.12.1

## Running locally

`uvicorn app:app --reload` to start the local server


## Deployment to Toolforge

1. `pip freeze > requirements.txt` to set dependencies (remember to run this every time I add a new dependency)
2. create a Procfile (see the tutorial for guidelines)
3. `ssh` into Toolforge, `become` the tool in question, `toolforge build start <repo url>`
4. wait for `toolforge build show` to return `ok(Succeeded)`
5. start the webservice with `toolforge webservice buildservice start --mount=none`

### Deployment troubleshooting
1. `toolforge build logs` will display the last build logs (useful in case a build failed)
2. `toolforge webservice --backend kubernetes buildservice logs` might reveal some information, in a case where the build passed, but the webservice does not work

For more information: https://wikitech.wikimedia.org/wiki/Help:Toolforge/Build_Service#Build_and_deploy


## Further development

Commands previously used in Toolhunt will work here, e.g. `kubectl get pods` to check pod status and `sql tools` to connect to the shared MariaDB instance


Questions:
1. How would I update a tool?  Do I need to rebuild from scratch?
   - The answer appears to be "yes, run `toolforge build start` with the repo name, then `toolforge webservice restart`"
   - As databases are hosted on Toolforge, this shouldn't have any implications
   - Need to check back on my Toolhunt documentation to figure out how to link everything up here

2. How would I run cronjobs and other things?  Need to see how to set up the db and run commands.

3. How could I incorporate Docker? (would that even be necessary for anything other than ease of local development?)


To do:
1. Incorporate a database, models & schemas
2. Incorporate Docker for local development, and figure out how to make it work with Toolforge
3. Incorporate poetry (Slavina says it's still a good idea - but as with Toolhunt, will need to push the contents of the .toml to requirements.txt) 