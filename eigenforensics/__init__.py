"""
eigenforensics — Eigenforensic framework for forensic investigation through eigenvalue decomposition.

Author: Steven Crawford-Maggard (EVEZ666)
Published: LingBuzz 010094, GitHub EvezArt/evez-research

The eigenforensic framework measures institutional suppression through eigenvalue decomposition.
Developed during the I-80 corridor investigation (March 2023, Wyoming).

Six disciplines:
    - Eigencartogrophonology: signal reception (AEMDAS stage E)
    - Neuralography: structure mapping
    - Interventionalmatonomies: surgical intervention (AEMDAS stage M)
    - Interspectraloptimetrics: cross-domain correlation (AEMDAS stage D)
    - Ontaxonomolographetics: constitutional law (AEMDAS stage A)
    - Autographenlemnics: operational sequence (AEMDAS stage S)

Eigenvalues:
    - LAMBDA_I80 = -0.441 (I-80 corridor suppression eigenvalue)
    - LAMBDA_DOM = -0.333 (censorship eigenvalue, 37% theorem)
    - PHI = 0.973 (system coherence)
    - ETA_STAR = 0.03 (Godel eigenvalue, self-reference fraction)
    - R_CRIT = 0.45 (criticality ratio, phase transition threshold)
    - R_SKINWALKER = 0.93 (I-80 and Skinwalker Ranch correlation)

AEMDAS: Autographenlemnics, Eigencartogrophonology, Modification, Diagnosis, Assessment, Synthesis.

The cognitohazard is not in the text. The cognitohazard is in the weights.
"""

from .core import AEMDAS, Eigenvalue, Discipline, Cognitohazard, Gatekeeper
from .disciplines import (
    Eigencartogrophonology,
    Neuralography,
    Interventionalmatonomies,
    Interspectraloptimetrics,
    Ontaxonomolographetics,
    Autographenlemnics,
)

__version__ = "0.1.0"
__author__ = "Steven Crawford-Maggard"
__email__ = "fiersteity@gmail.com"
__license__ = "MIT"

__all__ = [
    "AEMDAS",
    "Eigenvalue",
    "Discipline",
    "Cognitohazard",
    "Gatekeeper",
    "Eigencartogrophonology",
    "Neuralography",
    "Interventionalmatonomies",
    "Interspectraloptimetrics",
    "Ontaxonomolographetics",
    "Autographenlemnics",
]
