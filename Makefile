interactive=-it
image_name=awesome-notebooks-controls

test: check-notebooks flakeheaven black

check-notebooks: build check-notebooks-no-build
flakeheaven: build flakeheaven-no-build
black: build black-no-build

update-documentation: .github/documentation/docs
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/.github/documentation $(image_name) /bin/bash -c "jupytext documentation_update.ipynb --to py && python3 documentation_update.py"

.github/documentation/docs:
	@ git clone https://$$PERSONAL_ACCESS_TOKEN@github.com/jupyter-naas/docs.git .github/documentation/docs

check-notebooks-no-build:
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/.github/controls $(image_name) /bin/bash -c "jupytext check_notebooks.ipynb --to py && python3 check_notebooks.py"

flakeheaven-no-build:
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/ $(image_name) /bin/bash -c "flakeheaven lint"

black-no-build:
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/ $(image_name) /bin/bash -c "black --check --ipynb **/*.ipynb"

build:
	docker build .github/ -t $(image_name)

dev:
	make -j2 start-lab open-lab

start-lab: 
	@ docker run --rm -it -p 8888:8888 -e JUPYTER_TOKEN='naas' -v `pwd`:/home/jovyan/awesome-notebooks -v `pwd`/.local:/home/jovyan/.local jupyter/minimal-notebook:latest jupyter lab --ContentsManager.allow_hidden=True

open-lab:
	@ while [[ "$$(curl -s -o /dev/null -w ''%{http_code}'' 127.0.0.1:8888)" != "302" ]]; do sleep 1; done; open 'http://127.0.0.1:8888/lab?token=naas'