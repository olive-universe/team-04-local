---
name: code-simplification
description: Refactor and simplify code or plans for maximum clarity and maintainability without altering external behavior. Use when code feels overly complex, deeply nested, or bloated, or when applying Chesterton's Fence to eliminate unnecessary weight.
---

# Code Simplification

> *"Clarity over cleverness."*

Simplify implementation, architecture, and specifications without changing external contracts or functional behavior.

---

## 1. Core Principles

- **Chesterton's Fence:** Never delete or refactor a piece of logic or constraint until you fully understand why it was put there in the first place.
- **Clarity over Brevity:** The goal is not the fewest lines of code or densest syntax, but the easiest code for a human to read, trace, and debug 6 months from now.
- **Single Responsibility:** Flatten deep nesting, split multi-purpose functions, and separate policy from mechanism.

---

## 2. Refactoring Targets

- **Deep Nesting:** Replace nested `if`/`else` structures with early return guards.
- **Complex Conditionals:** Extract compound boolean expressions into well-named explanatory variables or helper functions.
- **Dead Code & Speculative Generality:** Remove uncalled functions, unused parameters, and over-engineered abstractions built for hypothetical future needs.
- **Long Procedures:** Break down lengthy procedural scripts into sequential, clearly named pipeline stages.

---

## 3. Simplification Checklist

- [ ] Does this change preserve 100% of existing behavior and test cases?
- [ ] Is the control flow flatter and easier to follow at a glance?
- [ ] Are variable and function names self-describing?
- [ ] Did we avoid introducing new external dependencies or abstractions?
