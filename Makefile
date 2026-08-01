SHELL := /bin/bash
.DEFAULT_GOAL := help

PYTHON  ?= python3
VERSION := $(shell grep -m1 '^version' pyproject.toml | sed -E 's/version = "(.*)"/\1/')
DIST    := dist
SIGNER  ?=

.PHONY: help venv install install-dev test lint format check \
        build sign clean distclean version tag release

help: ## Muestra esta ayuda
	@echo "pyfva - version actual: $(VERSION)"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

venv: ## Crea el entorno virtual con uv (.venv)
	uv venv

install: ## Instala las dependencias del proyecto
	uv pip install -r requirements.txt

install-dev: install ## Instala dependencias de desarrollo (test, lint)
	uv pip install pytest ruff wheel

test: ## Ejecuta la batería de pruebas (run_test.sh)
	./run_test.sh

lint: ## Revisa el estilo del código con ruff
	uv run ruff check pyfva

format: ## Formatea el código con ruff
	uv run ruff format pyfva

check: lint test ## Corre lint y pruebas

build: clean ## Genera sdist y wheel en dist/
	uv build

sign: build ## Firma con GPG los artefactos generados (requiere SIGNER=usuario@correo; PyPI ya no acepta .asc, usar para otros canales)
	@for f in $(DIST)/*.tar.gz $(DIST)/*.whl; do \
		gpg --detach-sign --armor $${SIGNER:+--local-user "$(SIGNER)"} "$$f"; \
	done

clean: ## Elimina artefactos de compilación y cachés
	rm -rf build *.egg-info pyfva.egg-info
	find . -name '__pycache__' -not -path './.venv/*' -exec rm -rf {} +
	find . -name '*.pyc' -not -path './.venv/*' -delete

distclean: clean ## Además elimina dist/
	rm -rf $(DIST)

version: ## Muestra la versión actual del proyecto
	@echo $(VERSION)

tag: ## Crea el tag git de la version actual (v$(VERSION))
	git tag -a v$(VERSION) -m "Version $(VERSION)"
	@echo "Tag v$(VERSION) creado. Ejecute 'git push origin v$(VERSION)' para publicarlo."

release: check build ## Corre check y build para dejar todo listo antes de publicar
	@echo "Artefactos listos en $(DIST)/ para la version $(VERSION)"
