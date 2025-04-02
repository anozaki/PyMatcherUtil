# Contains useful

.PHONY: pylint
pylint:
	@uv run -m pylint -j 4 src

.PHONY: mypy
mypy:
	@uv run -m mypy src

.PHONY: black
black:
	@uv run -m black --check src

.PHONY: pydocstyle
pydocstyle:
	@uv run -m pydocstyle src

.PHONY: pytest
pytest:
	@uv run pytest

.PHONY:
validate: black pylint pydocstyle mypy pytest
