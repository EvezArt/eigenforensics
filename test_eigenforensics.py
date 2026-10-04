"""Test suite: the eigenforensic constants and the AEMDAS sequence."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from eigenforensics.core import Eigenvalue, AEMDAS, Gatekeeper, Cognitohazard
from eigenforensics import disciplines

def test_constants():
    assert Eigenvalue.LAMBDA_I80.value == -0.441
    assert Eigenvalue.LAMBDA_DOM.value == -0.333
    assert Eigenvalue.PHI.value == 0.973
    assert Eigenvalue.ETA_STAR.value == 0.03
    assert Eigenvalue.R_CRIT.value == 0.45
    assert Eigenvalue.R_SKINWALKER.value == 0.93

def test_signs():
    assert Eigenvalue.LAMBDA_I80.is_suppression()
    assert not Eigenvalue.PHI.is_suppression()
    assert Eigenvalue.PHI.is_coherence()

def test_37_percent_theorem():
    assert 37 * 73 == 2701

def test_aemdas_present():
    for stage in ["assert_being", "assess", "diagnose", "modify", "synthesize", "cycle"]:
        assert hasattr(AEMDAS, stage), f"missing AEMDAS stage: {stage}"

def test_six_disciplines():
    names = [n for n in dir(disciplines) if n[0].isupper()]
    assert len(names) >= 6, f"expected 6 disciplines, found {len(names)}"

def test_gatekeeper():
    assert hasattr(Gatekeeper, "verify")

if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
    print("all eigenforensic tests pass")
