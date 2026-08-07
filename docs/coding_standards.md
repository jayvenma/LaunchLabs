## Coding Standards

- Follow PEP 8 conventions.
- Use Python type hints for public functions and methods.
- Use descriptive names instead of abbreviations unless the abbreviation is standard engineering notation.
- Use lowercase `snake_case` for files, functions, and variables.
- Use `PascalCase` for classes.
- Use `UPPER_CASE` for true constants.
- Prefer explicit, readable code over clever or highly condensed code.
- Public functions should include docstrings.
- Engineering functions must document:
  - Parameters
  - Return values
  - Units
  - Assumptions
  - Relevant equations or references when appropriate
- Avoid magic numbers. Physical constants belong in the constants package.
- Validate physically meaningful inputs where appropriate.
- Do not silently convert units.
- Use SI units internally.
- Use radians internally for angular calculations.
- Round values only for display, never during intermediate calculations.
- New engineering functionality should include tests.
- Ruff, Black, mypy, and pytest should pass before a change is considered complete.

Note: I am okay if you use AI in your work, however I ask that you review and understand what code you are putting in. 
      Furthermore, please cite which model of AI you used in your pull request.