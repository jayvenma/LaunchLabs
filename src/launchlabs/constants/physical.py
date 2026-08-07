"""
LaunchLab Physical Constants

This module contains universal physical constants used throughout LaunchLab.

Reference
---------
CODATA 2022 Recommended Values of the Fundamental Physical Constants
https://physics.nist.gov/cuu/Constants/

Units
-----
All values are stored in SI units.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PhysicalConstant:
    """
    Represents a universal physical constant.

    Attributes
    ----------
    name : str
        Full name of the constant.
    symbol : str
        Standard scientific symbol.
    value : float
        Numerical value in SI units.
    unit : str
        SI unit expressed using ASCII notation.
    description : str
        Brief explanation of the constant.
    reference : str
        Source of the constant's value.
    """

    name: str
    symbol: str
    value: float
    unit: str
    description: str
    reference: str


# ============================================================================
# Universal Physical Constants
# ============================================================================

G = PhysicalConstant(
    name="Newtonian Constant of Gravitation",
    symbol="G",
    value=6.67430e-11,
    unit="m^3 kg^-1 s^-2",
    description="Universal gravitational constant.",
    reference="CODATA 2022",
)

C = PhysicalConstant(
    name="Speed of Light in Vacuum",
    symbol="c",
    value=299_792_458.0,
    unit="m s^-1",
    description="Defined speed of light in vacuum.",
    reference="CODATA 2022",
)

STANDARD_GRAVITY = PhysicalConstant(
    name="Standard Gravity",
    symbol="g0",
    value=9.80665,
    unit="m s^-2",
    description="Standard acceleration due to gravity at Earth's surface.",
    reference="CGPM",
)

PLANCK = PhysicalConstant(
    name="Planck Constant",
    symbol="h",
    value=6.62607015e-34,
    unit="J s",
    description="Relates the energy of a photon to its frequency.",
    reference="CODATA 2022",
)

REDUCED_PLANCK = PhysicalConstant(
    name="Reduced Planck Constant",
    symbol="h_bar",
    value=1.054571817e-34,
    unit="J s",
    description="Planck constant divided by 2*pi.",
    reference="CODATA 2022",
)

BOLTZMANN = PhysicalConstant(
    name="Boltzmann Constant",
    symbol="k",
    value=1.380649e-23,
    unit="J K^-1",
    description="Relates thermal energy to temperature.",
    reference="CODATA 2022",
)

AVOGADRO = PhysicalConstant(
    name="Avogadro Constant",
    symbol="N_A",
    value=6.02214076e23,
    unit="mol^-1",
    description="Number of particles in one mole.",
    reference="CODATA 2022",
)

ELEMENTARY_CHARGE = PhysicalConstant(
    name="Elementary Charge",
    symbol="e",
    value=1.602176634e-19,
    unit="C",
    description="Magnitude of the electric charge of one proton.",
    reference="CODATA 2022",
)

VACUUM_PERMITTIVITY = PhysicalConstant(
    name="Vacuum Permittivity",
    symbol="epsilon_0",
    value=8.8541878128e-12,
    unit="F m^-1",
    description="Electric constant.",
    reference="CODATA 2022",
)

VACUUM_PERMEABILITY = PhysicalConstant(
    name="Vacuum Permeability",
    symbol="mu_0",
    value=1.25663706212e-6,
    unit="N A^-2",
    description="Magnetic constant.",
    reference="CODATA 2022",
)

STEFAN_BOLTZMANN = PhysicalConstant(
    name="Stefan-Boltzmann Constant",
    symbol="sigma",
    value=5.670374419e-8,
    unit="W m^-2 K^-4",
    description="Relates blackbody radiant power to temperature.",
    reference="CODATA 2022",
)

UNIVERSAL_GAS_CONSTANT = PhysicalConstant(
    name="Universal Gas Constant",
    symbol="R",
    value=8.314462618,
    unit="J mol^-1 K^-1",
    description="Universal gas constant.",
    reference="CODATA 2022",
)