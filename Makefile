interactive=-it

lint: build lint-no-build

lint-no-build:
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/.github/controls awesome-notebooks-controls /bin/bash -c "jupytext check_notebooks.ipynb --to py && python3 check_notebooks.py"

build:
	docker build .github/ -t awesome-notebooks-controls

dev:
	@ docker run --rm -it -p 8888:8888 -e JUPYTER_TOKEN='naas' -v `pwd`:/home/jovyan/awesome-notebooks -v `pwd`/.local:/home/jovyan/.local jupyter/minimal-notebook:latest jupyter lab --ContentsManager.allow_hidden=True