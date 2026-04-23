ZOLA_VERSION=v0.19.1

default: build

serve:
	docker run -u "$$(id -u):$$(id -g)" -v $$PWD:/app --workdir /app -p 1111:1111 ghcr.io/getzola/zola:$(ZOLA_VERSION) serve --interface 0.0.0.0 --base-url localhost

build:
	docker run -u "$$(id -u):$$(id -g)" -v $$PWD:/app --workdir /app ghcr.io/getzola/zola:v0.19.1 build

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
