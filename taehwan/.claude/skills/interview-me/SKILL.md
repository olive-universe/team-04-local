---
name: interview-me
description: Interrogate underspecified requests and extract underlying user intent through a structured one-question-at-a-time interview. Use when user requests lack context, when requirements are ambiguous, or when explicitly asked to "interview me", "grill me", or stress-test ideas before planning or implementation.
---

# Interview Me

Extract what the user *actually* wants and needs, rather than blindly building a literal, underspecified request.

---

## 1. When to Trigger

- A request is underspecified (e.g., *"Build an 안내 service"* without clear user context, constraints, or goals).
- The user explicitly asks: `/spec`, `"interview me"`, `"grill me"`, `"질문해줘"`, or `"stress-test my thinking"`.
- The agent catches itself filling in ambiguous assumptions before a clear spec or plan exists.

---

## 2. Interview Rules

1. **Ask Exactly ONE Question at a Time:** Never dump a bulleted list of 5 questions. Ask the single highest-leverage question, accompanied by a reasonable working guess.
2. **Listen for "Want vs. Should Want":** Distinguish between what the user thinks they ought to build versus the actual pain point they need resolved.
3. **Hypothesize with Confidence:** State an initial hypothesis with an estimated confidence percentage (e.g., *"I believe your priority is X (65% confidence). Is that right, or is Y more critical?"*).
4. **Restate Intent in User's Words:** Reflect the user's intent back to them to ensure complete alignment.
5. **Require Explicit Confirmation:** Do not move forward until reaching ~95% confidence and receiving an explicit confirmation from the user.
6. **Stop Rule:** When requirements are crystal clear, summarize the final scope and propose transitioning to the next phase (e.g., `/plan` or `/build`).

---

## 3. High-Leverage Question Patterns

- **Problem & Customer:** *"Who is the single primary user suffering from this, and what is the exact moment they get stuck?"*
- **Success Criteria:** *"What is the single measurable number we can count to prove this actually solved the problem?"*
- **Non-Goals / Scope:** *"What is explicitly OUT of scope for this first version that we will refuse to build right now?"*
- **Trade-offs:** *"If you have to choose between speed of launch and completeness of features, which one wins?"*
