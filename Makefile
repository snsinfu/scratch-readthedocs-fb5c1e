ARTIFACTS = \
  .venv \
  _venv.ok

.PHONY: all clean serve

all: _venv.ok
	@:

clean:
	rm -rf $(ARTIFACTS)

serve: docs/_build/html
	python3 -m http.server --directory docs/_build/html 8888

docs/_build/html: docs/*
	make -C docs html

_venv.ok: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	@touch $@
