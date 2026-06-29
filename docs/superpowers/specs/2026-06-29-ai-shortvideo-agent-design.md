# AI ShortVideo Agent Design

## Purpose

AI ShortVideo Agent is an open-source workflow kit for creators and small teams who use AI to plan, script, and operate short-video content across platforms such as Douyin, WeChat Channels, TikTok, and Bilibili.

The first release focuses on transparent, reusable workflows rather than a closed automation platform. It gives users prompts, process templates, sample briefs, and a small planning engine that turns a content brief into a practical production plan.

## Audience

- Individual creators who want repeatable short-video planning workflows.
- Small business operators who need scripts and publishing plans.
- AI builders who want examples of Codex-assisted content operations.
- Maintainers who want to contribute platform-specific workflows.

## Scope

The initial project includes:

- A README that explains the project, features, setup, and roadmap.
- Open-source governance files: license, contributing guide, code of conduct.
- Workflow documentation for Douyin, WeChat Channels, and enterprise promo videos.
- Prompt templates for trend analysis, script writing, and publishing calendars.
- Example input and output files.
- A small Python planner module with tests.
- An OpenAI Codex for Open Source application draft with honest early-stage metrics.

The project does not claim existing community traction. It presents itself as an early-stage open-source project that will be maintained publicly.

## Architecture

The repository is organized as a toolkit:

- `src/shortvideo_agent/` contains the reusable planning logic.
- `prompts/` contains model-agnostic prompt templates.
- `docs/workflows/` explains platform and content workflows.
- `examples/` shows practical inputs and outputs.
- `tests/` verifies the Python planning engine.

The first code module is intentionally small: it accepts a structured content brief and produces a plan with audience, platform, hook, script outline, assets, publishing notes, and review checks.

## Success Criteria

- A reviewer can open the repository and understand what the project does within one minute.
- The repository has enough real content to be useful as a starting point.
- The example planner can be tested locally.
- The application draft is accurate and does not exaggerate stars, forks, downloads, or production usage.

