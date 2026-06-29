from dataclasses import dataclass
from typing import Dict, List


class BriefValidationError(ValueError):
    """Raised when a content brief is missing required planning fields."""


@dataclass(frozen=True)
class ContentBrief:
    topic: str
    audience: str
    platform: str
    goal: str
    tone: str
    duration_seconds: int


@dataclass(frozen=True)
class ContentPlan:
    topic: str
    audience: str
    platform: str
    goal: str
    hook: str
    script_outline: List[str]
    asset_checklist: List[str]
    publishing_notes: List[str]
    review_checks: List[str]


PLATFORM_NOTES: Dict[str, List[str]] = {
    "douyin": [
        "Use a direct 3-second hook and keep the first visual highly specific.",
        "Add a comment prompt that invites viewers to ask for the checklist.",
        "Review the caption for search keywords and local business terms.",
    ],
    "wechat_channels": [
        "Open with a trust-building claim before moving into the practical steps.",
        "Use a softer call to action that encourages saves and sharing.",
        "Keep the caption useful enough to stand alone in a private-share context.",
    ],
    "tiktok": [
        "Use a globally understandable hook and avoid platform-specific jargon.",
        "Keep subtitles concise and readable on mobile.",
        "Add a repeatable series title if the topic can become a content column.",
    ],
    "bilibili": [
        "Frame the video as a useful mini tutorial with a clear takeaway.",
        "Use chapter-like pacing so viewers can follow the explanation.",
        "Invite viewers to comment with their workflow or use case.",
    ],
}


def build_content_plan(brief: ContentBrief) -> ContentPlan:
    _validate_brief(brief)
    platform = _normalize_platform(brief.platform)
    notes = PLATFORM_NOTES.get(
        platform,
        [
            "Use a general short-video structure: hook, context, steps, proof, call to action.",
            "Adapt caption length and call to action to the publishing platform.",
            "Check whether the platform rewards comments, saves, shares, or watch time most.",
        ],
    )

    hook = (
        f"Show {brief.audience} one concrete way to use {brief.topic} "
        f"to {brief.goal}."
    )

    script_outline = [
        f"3-second hook: name the pain point and promise a practical result for {brief.audience}.",
        f"Context: explain why {brief.topic} matters now in one sentence.",
        "Method: show three repeatable steps with one visual example per step.",
        f"Proof: describe the expected outcome connected to the goal: {brief.goal}.",
        "Call to action: ask viewers to comment, save, or request the workflow template.",
    ]

    asset_checklist = [
        "One cover image with the core promise in fewer than nine words.",
        "A-roll talking points or voiceover script.",
        "Three supporting screenshots, clips, or screen recordings.",
        "Subtitle file or burned-in captions.",
        "Caption draft with keywords and call to action.",
    ]

    review_checks = [
        "The first three seconds communicate the value clearly.",
        "Every claim is either demonstrated or framed as a recommendation.",
        "The script can be filmed within the target duration.",
        "The call to action matches the audience and platform.",
        "No private customer data, credentials, or copyrighted media are exposed.",
    ]

    return ContentPlan(
        topic=brief.topic.strip(),
        audience=brief.audience.strip(),
        platform=platform,
        goal=brief.goal.strip(),
        hook=hook,
        script_outline=script_outline,
        asset_checklist=asset_checklist,
        publishing_notes=notes,
        review_checks=review_checks,
    )


def _validate_brief(brief: ContentBrief) -> None:
    required_fields = {
        "topic": brief.topic,
        "audience": brief.audience,
        "platform": brief.platform,
        "goal": brief.goal,
        "tone": brief.tone,
    }

    missing = [name for name, value in required_fields.items() if not value.strip()]
    if missing:
        raise BriefValidationError(f"Missing required field: {missing[0]}")

    if brief.duration_seconds < 15 or brief.duration_seconds > 180:
        raise BriefValidationError("duration_seconds must be between 15 and 180")


def _normalize_platform(platform: str) -> str:
    return platform.strip().lower().replace("-", "_").replace(" ", "_")

