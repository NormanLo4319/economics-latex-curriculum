"""Independently recompute every number used in Micro Chapter 3 and its quiz.

Run: python tools/check_math.py
Exits non-zero if any value disagrees. This is a review aid, not a substitute for
instructor review.
"""
from fractions import Fraction as F
import sys

fails = []


def eq(a, b, c, d):
    """Equilibrium for Qd = a - bP, Qs = c + dP."""
    p = F(a - c, b + d)
    q = a - b * p
    assert q == c + d * p, "supply and demand disagree"
    return p, q


def check(label, got, want):
    ok = got == want
    print(("ok   " if ok else "FAIL ") + f"{label}: got {got}, want {want}")
    if not ok:
        fails.append(label)


# Chapter worked example and quiz Q6
check("base eq (120,4,20,6)", eq(120, 4, 20, 6), (10, 80))
check("shortage at P=8", (120 - 4 * 8) - (20 + 6 * 8), 20)
check("surplus at P=12", (20 + 6 * 12) - (120 - 4 * 12), 20)
check("demand up a=160", eq(160, 4, 20, 6), (14, 104))
check("supply down c=0", eq(120, 4, 0, 6), (12, 72))
check("both a=160,c=0", eq(160, 4, 0, 6), (16, 96))
check("supply up c=40", eq(120, 4, 40, 6), (8, 88))
# Chapter practice problems
check("practice 1", eq(200, 5, 50, 10), (10, 150))
check("practice 2", eq(230, 5, 50, 10), (12, 170))
# Quiz Q5 and its distractors
check("Q5 correct", eq(90, 3, 10, 5)[0], 10)
check("Q5 distractor adds intercepts", F(90 + 10, 3 + 5), F(25, 2))
check("Q5 distractor subtracts slopes", F(90 - 10, 5 - 3), 40)
check("Q5 distractor sign flip", F(10 - 90, 3 + 5), -10)
# General formulas
for a, b, c, d in [(120, 4, 20, 6), (90, 3, 10, 5), (200, 5, 50, 10)]:
    p, q = eq(a, b, c, d)
    check(f"formula Q* ({a},{b},{c},{d})", q, F(a * d + b * c, b + d))

sys.exit(1 if fails else 0)
