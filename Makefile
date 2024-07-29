install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		python -m textblob.download_corpora

format:
	black *.py nlplogic/*.py

lint:
	pylint --disable=R,C *.py nlplogic/*.py

all: install format lint 