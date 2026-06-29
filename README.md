# AI ShortVideo Agent

AI ShortVideo Agent is an open-source workflow kit for planning, scripting, and operating short-video content with AI.

The project is designed for creators, local businesses, and AI builders who want repeatable workflows for Douyin, WeChat Channels, TikTok, Bilibili, and enterprise promo videos. It combines prompt templates, platform workflows, examples, and a small tested planning engine.

> Status: early-stage open source project. The repository is intentionally transparent about its current maturity and roadmap.

## What It Does

- Turns a short content brief into a practical production plan.
- Provides reusable prompts for trend analysis, video scripts, and publishing calendars.
- Documents platform-specific workflows for short-video operations.
- Shows how Codex-assisted development can support content operations.
- Gives contributors a focused place to add workflows, templates, and examples.

## Quick Start

Run the planner with the sample brief:

```bash
PYTHONPATH=src python3 -m shortvideo_agent.cli examples/brief.yaml
```

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## License

MIT License.
