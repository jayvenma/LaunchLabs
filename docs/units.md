# Units Policy

## Purpose

LaunchLab uses the International System of Units (SI) as its internal engineering standard.

All calculations, stored constants, and engineering models are expected to use SI units unless explicitly documented otherwise.

This policy exists to ensure consistency, reduce ambiguity, and prevent unit conversion errors.

---

# General Principles

- SI units are the default throughout LaunchLab.
- Internal calculations should never mix unit systems.
- Unit conversions should occur only at explicit input or output boundaries.
- Public documentation should always state the units of inputs and outputs.
- Variables should make units obvious whenever ambiguity exists.

---

# Base Units

| Quantity | Unit | Symbol |
|----------|------|--------|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric Current | ampere | A |
| Temperature | kelvin | K |
| Amount of Substance | mole | mol |
| Luminous Intensity | candela | cd |

---

# Derived Units

| Quantity | Unit | Symbol |
|----------|------|--------|
| Force | newton | N |
| Energy | joule | J |
| Power | watt | W |
| Pressure | pascal | Pa |
| Frequency | hertz | Hz |
| Charge | coulomb | C |

---

# Angular Units

Internally:

- Radians

For presentation:

- Degrees may be displayed when easier for humans to understand.

Example:

```python
launch_angle_rad = math.pi / 4
```

Avoid storing angles in degrees inside engineering calculations.

---

# Distance

Internal:

- meters

Presentation may include:

- kilometers
- astronomical units
- light-years

Conversions should be performed explicitly.

---

# Velocity

Internal:

- meters per second (m/s)

Avoid storing:

- km/h
- mph

These may be converted for display if needed.

---

# Acceleration

Internal:

- m/s²

---

# Mass

Internal:

- kilograms

Avoid:

- pounds
- slugs

---

# Time

Internal:

- seconds

Presentation may use:

- minutes
- hours
- days

Engineering calculations should convert these to seconds first.

---

# Temperature

Internal:

- kelvin

Presentation may display:

- Celsius
- Fahrenheit

Conversions should only occur for user interaction.

---

# Pressure

Internal:

- pascals

Presentation may convert to:

- bar
- psi
- atmospheres

---

# Energy

Internal:

- joules

---

# Power

Internal:

- watts

---

# Variable Naming

When units are not immediately obvious, include them in the variable name.

Examples:

```python
radius_m
velocity_m_s
temperature_K
pressure_Pa
mass_kg
```

Avoid ambiguous names such as:

```python
radius
speed
time
```

unless the surrounding context makes the units explicit.

---

# Physical Constants

All constants stored within LaunchLab shall use SI units.

Example:

```python
EARTH_RADIUS = 6_371_008.8  # meters
```

---

# User Input

LaunchLab may accept non-SI units from users in future interfaces.

Inputs should be converted immediately into SI units before any calculations begin.

---

# User Output

Results may be displayed in units that improve readability.

Examples:

- kilometers instead of meters
- degrees instead of radians
- hours instead of seconds

Engineering calculations should never depend on these presentation units.

---

# Future Considerations

Future versions of LaunchLab may incorporate a unit-handling library such as Pint.

Until then, unit correctness is enforced through documentation, naming conventions, testing, and code review.

---

# Summary

LaunchLab follows one fundamental rule:

> **Calculate in SI. Convert only for people.**