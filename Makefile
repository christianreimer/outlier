.PHONY: test clean install perf

test: 
	pytest --cov-report term-missing --cov=runstat.py --cov=outlier.py --verbose tests/*

clean:
	@echo "Removing cache directories"
	@find . -name __pycache__ -type d -exec rm -rf {} +
	@find . -name .cache -type d -exec rm -rf {} +
	@find . -name .coverage -delete

install:
	pip install -r requirements.txt
	pip install -r requirements_test.txt

perf:
	python -m tests.perf
