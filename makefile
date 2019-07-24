IMAGE_NAME='Project'
BUILD=1
VERSION=1.0.$(BUILD)

all: clean build test

restore:
	pip install -r requirements.txt

python-test:

lint: python-build

python-build:
	find . -name "*.py" -print0 | xargs -0 pylint 2>&1 | tee pylint.err


build: restore python-build

test: python-test

run:
	python3 src/main.py

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf $(find . -type d -name .pytest_cache)
