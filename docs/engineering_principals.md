## Floating-Point Policy

- Do not compare floating-point values using exact equality unless the value is mathematically discrete or intentionally exact.
- Use `math.isclose()` or `numpy.isclose()` for scalar and array comparisons.
- Default relative tolerance: `1e-9`
- Default absolute tolerance: `1e-12`
- Tests involving published engineering reference values may define their own tolerance when justified.
- Tolerances must be documented when they are looser than the project default.
- Avoid rounding intermediate calculations. Round only for presentation.