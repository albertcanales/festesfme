default: build

serve:
	zola serve

build:
	zola build

install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

zip: build
	cd public/ && zip -r ../festes.zip *

designs:
	.venv/bin/python src/designs.py

designs-debug:
	.venv/bin/python src/designs.py -vdb

clean-designs:
	rm -rf static/festes*/samarretes

clean-zip:
	rm festes.zip

clean: clean-designs clean-zip
