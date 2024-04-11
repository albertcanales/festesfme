default: build

serve:
	zola serve

build:
	zola build

install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

designs:
	.venv/bin/python src/designs.py

designs-debug:
	.venv/bin/python src/designs.py -v
