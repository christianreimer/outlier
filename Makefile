.PHONY: test timeit clean install

test: 
	pytest --cov-report term-missing --cov=. --verbose tests/*

timeit:	
	@echo "Timing add()"
	@python -m timeit -s 'import median, random; m = median.RunningMedian(101)' 'm.add(random.random())'
	@echo ""
	@echo "Timing median()"
	@python -m timeit -s 'import median, random; m = median.RunningMedian(101); [m.add(random.random()) for _ in range(102)]' 'm.median()'

clean:
	@echo "Removing cache directories"
	@find . -name __pycache__ -type d -exec rm -rf {} +
	@find . -name .cache -type d -exec rm -rf {} +
	@find . -name .coverage -delete

install:
	pip install -r requirements.txt
	pip install -r requirements_test.txt
