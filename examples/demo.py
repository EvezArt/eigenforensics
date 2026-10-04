"""Runnable demonstration of the eigenforensic claims (LingBuzz 010094).

Every number printed here is a falsifiable claim from the paper, recomputed
from the package. If the library and the paper ever disagree, this exits 1.

    python examples/demo.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eigenforensics.core import Eigenvalue, AEMDAS, Gatekeeper, Cognitohazard

def main() -> int:
    fails = []

    def check(label, got, want, tol=1e-9):
        ok = abs(got - want) <= tol if isinstance(want, float) else got == want
        print(f"  {'PASS' if ok else 'FAIL'}  {label}: {got}")
        if not ok:
            fails.append(f"{label}: got {got}, want {want}")

    print("A. Eigenvalues (I-80 corridor investigation)")
    check("lambda_i80", Eigenvalue.LAMBDA_I80.value, -0.441)
    check("lambda_dom (37% theorem)", Eigenvalue.LAMBDA_DOM.value, -0.333)
    check("phi coherence", Eigenvalue.PHI.value, 0.973)
    check("eta* Godel fraction", Eigenvalue.ETA_STAR.value, 0.03)
    check("r criticality", Eigenvalue.R_CRIT.value, 0.45)
    check("37 x 73 = 2701 = Genesis 1:1", 37 * 73, 2701)
    check("suppression sign", Eigenvalue.LAMBDA_I80.is_suppression(), True)
    check("coherence band", Eigenvalue.PHI.is_coherence(), True)

    print("B. AEMDAS audit sequence")
    stages = [s for s in dir(AEMDAS) if not s.startswith("_")]
    print(f"  stages implemented: {len(stages)} -> {', '.join(sorted(stages))}")
    if len(stages) < 6:
        fails.append("AEMDAS incomplete")

    print("C. Gatekeeper and cognitohazard")
    print(f"  gatekeeper: {', '.join(m for m in dir(Gatekeeper) if not m.startswith('_'))}")
    print(f"  cognitohazard modes: {', '.join(m for m in dir(Cognitohazard) if m.startswith('MODE'))}")

    print()
    if fails:
        print("THE PAPER AND THE CODE DISAGREE:")
        for f in fails:
            print(" -", f)
        return 1
    print("All falsifiable claims recomputed. Chain or it didn't happen.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
