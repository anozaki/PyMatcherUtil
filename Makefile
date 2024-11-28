# Contains useful

.PHONY: pylint
pylint:
	@python3 -m pylint -j 4 src

.PHONY: mypy
mypy:
	@python3 -m mypy src

.PHONY: black
black:
	@python3 -m black --check src

.PHONY: pydocstyle
pydocstyle:
	@python3 -m pydocstyle src

.PHONY:
validate: black pylint mypy