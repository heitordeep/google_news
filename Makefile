SHELL=/bin/bash

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

# ------ Code style ------

style:  ## Run isort and black auto formatting code style in the project
	@isort .
	@black -S -t py37 -l 79 . --exclude '/(\.git|\.venv|env|venv|build|dist)/'

style-check:  ## Check isort and black code style
	@black -S -t py37 -l 79 --check . --exclude '/(\.git|\.venv|env|venv|build|dist)/'

clean:  ## Clean python bytecodes, optimized files, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo 'Temporary files deleted'

# ------ Installation requirements ------

requirements: ## Install project packages system
	@pip install --upgrade pip
	@pip install -r requirements/requirements.txt

xml: clean ## Get xml data from Google news.
	@python control/google_news.py

crawl: clean ## Crawl google site.
	@python control/crawl_google_news.py $(word)
