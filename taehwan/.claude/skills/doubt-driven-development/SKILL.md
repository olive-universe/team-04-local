---
name: doubt-driven-development
description: Apply adversarial skepticism and systematic disproof to non-trivial engineering decisions, unverified assumptions, and high-risk claims before finalizing changes. Use when evaluating critical logic, architecture boundaries, irreversible changes, or when unverified assumptions need rigorous fact-checking.
---

# Doubt-Driven Development

> *"A confident answer is not a correct one."*

Unlike post-implementation reviews, Doubt-Driven Development is an **in-flight, adversarial verification posture**. It prevents AI agents and engineers from quietly turning unverified assumptions into accepted "facts" across long working sessions.

---

## 1. When to Apply Doubt

Apply doubt specifically to **non-trivial decisions**:
- Introduces or modifies branching, control flow, or state-management logic.
- Crosses a module, component, database, or service boundary.
- Asserts a property that compilers, linters, or type systems cannot automatically guarantee (e.g., race conditions, idempotency, thread-safety, ordering invariants).
- Correctness relies on implicit context or unverified external assumptions.
- Has an irreversible blast radius (e.g., schema migrations, public API contracts, production deployments).

**Do NOT apply doubt to:**
- Routine formatting, mechanical edits, trivial refactors.
- Explicit, unambiguous user requirements.
- Low-risk, isolated changes with obvious correctness.

---

## 2. The 5-Step Doubt Cycle

1. **CLAIM:** State the core engineering decision or assumption explicitly in 2–3 clear sentences.
2. **EXTRACT:** Isolate the smallest reviewable unit (the artifact/snippet plus its operational contract).
3. **DOUBT:** Adopt a fresh-context persona biased toward **disproof rather than approval**:
   - Actively hunt for counter-examples, edge cases, race conditions, and silent failure modes.
   - Ask: *"Under what exact inputs or timing does this assumption break?"*
   - Demand concrete evidence/citations for any claimed behavior or performance metric.
4. **RECONCILE:** Evaluate the reviewer findings against reality:
   - Dismiss irrelevant noise or purely theoretical edge cases outside operational boundaries.
   - Directly resolve and fix all valid failure modes.
5. **STOP:** Enforce bounded cycles (maximum 2 passes) to prevent infinite loops of skepticism over minor details.

---

## 3. Fact-Checking Checklist

- [ ] Is there an unverified assumption being treated as established fact?
- [ ] Are claimed numbers, dates, or behaviors backed by an exact, verifiable source?
- [ ] What is the worst-case failure mode if this assumption is wrong?
- [ ] Has the solution been tested against the identified failure mode?
