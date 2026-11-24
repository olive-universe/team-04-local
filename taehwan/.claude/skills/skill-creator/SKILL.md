---
name: skill-creator
description: Create new custom agent skills, structure SKILL.md packages, and optimize skill triggers. Use when designing a new skill from scratch, editing or refining existing skills, or optimizing frontmatter descriptions for precise progressive disclosure.
---

# Skill Creator

Guide the design, structure, and optimization of modular AI agent skills adhering to the open `agentskills.io` standard.

---

## 1. Skill Anatomy

A skill is a self-contained folder containing at minimum a `SKILL.md`:
```text
.claude/skills/<skill-name>/
├── SKILL.md                 # Required: YAML frontmatter + structured guidelines
├── scripts/                 # Optional: Executable automation or validation scripts
└── references/              # Optional: Templates, examples, or detailed docs
```

### Frontmatter Schema
```yaml
---
name: <kebab-case-name>
description: <What this skill does and the exact triggering conditions. Be specific so the agent knows when to invoke it.>
---
```

---

## 2. Progressive Disclosure Principle

- Keep `description` informative and trigger-focused: agents evaluate the description to decide whether to read the full skill.
- Keep the main `SKILL.md` body concise, operational, and actionable.
- Offload deep reference materials, large lookup tables, and scripts to subdirectories (`references/`, `scripts/`) to preserve agent context.

---

## 3. Skill Authoring Steps

1. **Define Intent & Role:**
   - What specific capability does this skill grant?
   - What mistakes or antipatterns must it prevent?
2. **Determine Triggers:**
   - Write a clear, scenario-rich `description` in YAML frontmatter.
3. **Establish Constraints & Rules:**
   - Define "When to use" vs "When NOT to use".
   - Include clear positive examples ("Good") and negative examples ("Bad").
4. **Define Verification / Checklist:**
   - Add a tangible exit checklist for the agent to review before concluding its turn.
