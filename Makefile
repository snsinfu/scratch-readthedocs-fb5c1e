ARTIFACTS = \
  .venv \
  _venv.ok


.PHONY: all clean serve

all: _venv.ok
	@:

clean:
	rm -rf $(ARTIFACTS)

serve: docs/_build/html
	cd docs/_build/html; python3 -m http.server -b 127.0.0.1 8888

docs/_build/html: docs/*
	. .venv/bin/activate; $(MAKE) -C docs html

_venv.ok: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	@touch $@
