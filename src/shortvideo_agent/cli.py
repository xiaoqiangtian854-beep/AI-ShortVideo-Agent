import sys
from pathlib import Path

from .planner import BriefValidationError, ContentBrief, build_content_plan


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 -m shortvideo_agent.cli examples/brief.yaml")
        return 2

    try:
        brief = _load_brief(Path(sys.argv[1]))
        plan = build_content_plan(brief)
    except (BriefValidationError, OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(_render_plan(plan))
    return 0


def _load_brief(path: Path) -> ContentBrief:
    values = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid brief line: {raw_line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')

    return ContentBrief(
        topic=values.get("topic", ""),
        audience=values.get("audience", ""),
        platform=values.get("platform", ""),
        goal=values.get("goal", ""),
        tone=values.get("tone", ""),
        duration_seconds=int(values.get("duration_seconds", "60")),
    )


def _render_plan(plan) -> str:
    sections = [
        "# Content Plan",
        "",
        f"Topic: {plan.topic}",
        f"Audience: {plan.audience}",
        f"Platform: {plan.platform}",
        f"Goal: {plan.goal}",
        "",
        "## Hook",
        plan.hook,
        "",
        "## Script Outline",
        *_numbered(plan.script_outline),
        "",
        "## Asset Checklist",
        *_bullets(plan.asset_checklist),
        "",
        "## Publishing Notes",
        *_bullets(plan.publishing_notes),
        "",
        "## Review Checks",
        *_bullets(plan.review_checks),
    ]
    return "\n".join(sections)


def _numbered(items):
    return [f"{index}. {item}" for index, item in enumerate(items, start=1)]


def _bullets(items):
    return [f"- {item}" for item in items]


if __name__ == "__main__":
    raise SystemExit(main())

