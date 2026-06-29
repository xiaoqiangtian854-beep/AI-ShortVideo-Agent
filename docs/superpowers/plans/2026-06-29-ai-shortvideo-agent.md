# AI ShortVideo Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a real early-stage open-source repository for an AI short-video operations workflow kit.

**Architecture:** The repository combines documentation, reusable prompts, workflow examples, and a small tested Python planning engine. The code stays intentionally compact so the first public release is easy to understand and maintain.

**Tech Stack:** Python 3.10+, unittest, Markdown, YAML examples.

---

### Task 1: Project Foundation

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `CONTRIBUTING.md`
- Create: `CODE_OF_CONDUCT.md`
- Create: `.gitignore`

- [ ] Add a clear project overview, feature list, setup steps, and roadmap.
- [ ] Add MIT License so the project is open-source friendly.
- [ ] Add contribution and conduct docs for public collaboration.

### Task 2: Planning Engine

**Files:**
- Create: `pyproject.toml`
- Create: `src/shortvideo_agent/__init__.py`
- Create: `src/shortvideo_agent/planner.py`
- Create: `src/shortvideo_agent/cli.py`
- Create: `tests/test_planner.py`

- [ ] Write tests for brief validation and content plan generation.
- [ ] Run tests and confirm they fail before implementation.
- [ ] Implement the planner and CLI.
- [ ] Run tests and confirm they pass.

### Task 3: Workflow And Prompt Library

**Files:**
- Create: `docs/workflows/douyin-operations.md`
- Create: `docs/workflows/wechat-channels.md`
- Create: `docs/workflows/enterprise-promo.md`
- Create: `prompts/trend-analysis.md`
- Create: `prompts/video-script.md`
- Create: `prompts/publishing-calendar.md`

- [ ] Add platform workflows that map research, script, production, publishing, and review.
- [ ] Add prompt templates that can work with OpenAI, local models, or other AI tools.

### Task 4: Examples And Application Draft

**Files:**
- Create: `examples/brief.yaml`
- Create: `examples/trend-report.json`
- Create: `examples/sample-output.md`
- Create: `docs/openai-codex-oss-application.md`
- Create: `docs/roadmap.md`

- [ ] Add example inputs and outputs.
- [ ] Add a truthful OpenAI application draft with early-stage project wording.
- [ ] Add a public maintenance roadmap.

### Task 5: Verification

**Commands:**
- `PYTHONPATH=src python3 -m unittest discover -s tests`
- `python3 -m shortvideo_agent.cli examples/brief.yaml`

- [ ] Confirm tests pass.
- [ ] Confirm the CLI prints a usable production plan.
- [ ] Inspect the repository file list.
