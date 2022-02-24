interactive=-it

lint: build lint-no-build

lint-no-build:
	docker run --rm $(interactive) -v `pwd`:/data --workdir /data/.github/controls awesome-notebooks-controls /bin/bash -c "jupytext check_notebooks.ipynb --to py && python3 check_notebooks.py"

build:
	docker build .github/ -t awesome-notebooks-controls

dev:
	make -j2 start-lab open-lab

start-lab: 
	@ docker run --rm -it -p 8888:8888 -e JUPYTER_TOKEN='naas' -v `pwd`:/home/jovyan/awesome-notebooks -v `pwd`/.local:/home/jovyan/.local jupyter/minimal-notebook:latest jupyter lab --ContentsManager.allow_hidden=True

open-lab:
	@ while [[ "$$(curl -s -o /dev/null -w ''%{http_code}'' 127.0.0.1:8888)" != "302" ]]; do sleep 1; done; open 'http://127.0.0.1:8888/lab?token=naas'