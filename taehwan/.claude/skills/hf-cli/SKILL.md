---
name: hf-cli
description: Interact with the Hugging Face Hub via the official modern hf CLI. Use to search open-source models and datasets, inspect model cards and files, download model weights, manage datasets, launch or manage Hugging Face Spaces, and run remote cloud jobs.
---

# Hugging Face CLI (`hf-cli`)

Guide the AI coding agent in discovering, managing, and interacting with models, datasets, and Spaces on the **Hugging Face Hub** using the modern `hf` CLI.

---

## 1. Core CLI Commands

### Authentication
```bash
# Check login status
hf auth status

# Log in using a Hugging Face user access token
hf auth login --token <HF_TOKEN>
```

### Models & Search
```bash
# Search for models by keyword, task, or pipeline tag
hf models search <keyword> --limit 10

# Inspect model details, configuration, and README
hf models info <model_id>

# Download model repository or specific files locally
hf download <model_id> [filename] --local-dir <path>
```

### Datasets
```bash
# Search for datasets
hf datasets search <keyword> --limit 10

# Inspect dataset metadata, splits, and columns
hf datasets info <dataset_id>

# Download dataset
hf download --repo-type dataset <dataset_id> --local-dir <path>
```

### Spaces & Remote Jobs
```bash
# Inspect a Hugging Face Space (Gradio / Streamlit / Docker)
hf spaces info <space_id>

# Run or monitor remote training/inference jobs
hf jobs list
hf jobs status <job_id>
```

---

## 2. Best Practices for Coding Agents

1. **Verify Token Permissions:** When uploading datasets or writing to Hub repositories, confirm the user's Hugging Face token has `write` scope.
2. **Prefer Small / Quantized Weights:** When running models locally on developer machines, check for GGUF, AWQ, or smaller parameter variants (e.g., 0.5B ~ 7B).
3. **Use Official Datasets:** Prioritize verified community datasets with clear licensing and provenance.
