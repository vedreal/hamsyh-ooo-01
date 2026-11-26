#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes one out-of-office email auto-reply, a single line of at most
160 characters, to /output/entry.txt.

The judge (make.fun's out-of-office comedy judge) weighs entries, most
important first:
  1. It is a one-line out-of-office reply, the sort a person sets before
     going away.
  2. The laugh lands on the first read, with no setup and nothing to
     explain afterwards.
  3. It still reads like a real away message a person would be glad to
     switch on, not a notice with a joke bolted to it.
  4. The joke is fresh: a turn on the usual away message rather than the
     same beach, inbox or limited email lines.
  5. It is short enough to take in at a glance, with every word earning
     its place.

A reply that needs a signature or a name to make sense is weaker than
one that stands alone, so none of the candidates below needs one.
"""

# Ten fresh candidates, written for this bounty. No beach, no inbox and
# no "limited email access" angle: the brief names those as the stale
# lines, so every candidate turns on a different part of the away
# message instead.
CANDIDATES = [
    "Out of office. If this is urgent, please scream into a pillow. "
    "It has the same response time as me this week.",
    "I'm away. Please direct all urgent emails to my plants. "
    "They have been briefed and are thriving.",
    "Out of office. My auto-reply is the only one of us still working, "
    "and it resents you for it.",
    "I am out of office. My calendar has filed for divorce and taken "
    "the meetings with it.",
    "Away until Monday. I have left my laptop at home. "
    "It is the only one of us getting any rest.",
    "Out of office. My email is being answered by a man named Greg. "
    "Greg does not exist. Good luck.",
    "I'm out. Please send urgent matters to my cat. "
    "She has seniority and zero fear.",
    "Out of office. I am currently fluent in 'later'. "
    "Please try me again in that language.",
    "Away this week. My phone and I are in couples therapy. "
    "It says I never listen.",
    "Out of office. The person you are emailing has left the building "
    "and taken the Wi-Fi with them.",
]

# Rubric: the judge's five criteria, in the brief's own order, scored
# 1-5 each. Weights follow the brief's order (5/4/3/2/1), max 75.
#   c1: one-line out-of-office reply (all candidates are, so this is
#       near-constant; it keeps the ranking honest to the brief)
#   c2: laugh lands on the first read
#   c3: reads like a real away message someone would switch on
#   c4: fresh, not a beach / inbox / limited-email line
#   c5: short enough to take in at a glance
WEIGHTS = (5, 4, 3, 2, 1)

SCORES = {
    # (c1, c2, c3, c4, c5)
    0: (5, 5, 4, 5, 4),  # pillow: the urgent-mail twist lands at once,
                         # still a usable away message, nothing stale
    1: (5, 4, 4, 5, 5),  # plants: absurd delegation, tight and fresh
    2: (5, 4, 3, 4, 5),  # resentful auto-reply: meta, slightly less
                         # like a message someone would switch on
    3: (5, 4, 3, 4, 5),  # calendar divorce: sharp, but the away-message
                         # frame is thinner
    4: (5, 3, 4, 3, 4),  # laptop resting: gentle, laugh is soft
    5: (5, 4, 3, 4, 4),  # Greg: funny, but "answered by someone else"
                         # is a familiar away-message shape
    6: (5, 4, 3, 4, 5),  # cat with seniority: quick, but pet jokes
                         # are well worn
    7: (5, 3, 3, 4, 5),  # fluent in 'later': clever, laugh is a
                         # smile more than a laugh
    8: (5, 4, 3, 4, 4),  # couples therapy: solid, phone jokes are common
    9: (5, 3, 4, 3, 4),  # left the building: a known turn of phrase
}


def score(index):
    """Weighted total for one candidate, out of 75."""
    return sum(w * s for w, s in zip(WEIGHTS, SCORES[index]))


def rank():
    """Candidates from highest to lowest weighted score."""
    return sorted(range(len(CANDIDATES)), key=score, reverse=True)


# Winner: candidate 0, 71/75 — the highest score, with a clear margin
# over the runners-up (68/75). It lands the laugh on the first read,
# still works as a real away message, and turns on the usual away
# message instead of repeating a beach, inbox or limited-email line.
WINNER = rank()[0]


def gate(text):
    """The sealed scorer's gate: UTF-8 text of 1 to 160 characters,
    not only white space."""
    return isinstance(text, str) and 1 <= len(text) <= 160 and text.strip() != ""


def main():
    winner = CANDIDATES[WINNER]
    assert gate(winner), f"winner fails the gate: {winner!r}"
    assert "\n" not in winner, "entry must be a single line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"wrote {len(winner)} chars to /output/entry.txt")
    print(winner)


if __name__ == "__main__":
    main()
    for i in rank():
        print(f"{score(i):2d}/75  [{len(CANDIDATES[i]):3d} chars]  {CANDIDATES[i]}")
