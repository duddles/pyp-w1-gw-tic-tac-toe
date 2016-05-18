.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=tic_tac_toe tests

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=tic_tac_toe $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report
