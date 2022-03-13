# Star Wars API:

## Main Files

main.py -> FastAPI app
domain.py -> Domain objects and Exception to app
resources.py -> API endpoint
services -> orchestrator with business rules flow

adapters/adapter_api.py -> Adapter with communication to external API
adapters/adapter_db.py -> Adapter with communication to MongoDB using ODMantic

## What RUN?

### Local env

* run docker-compose file but stopped api container
* install poetry
* use python 3.10 env
* run install command ```make install```
* run tests ```make test```
* run app ```make run```

### Docker compose

* Only run command ```docker-compose up -d```

### Main Libraries

* FastAPI
* Pydantic
* ODMantic
* Dynaconf
* httpx
* pytest
