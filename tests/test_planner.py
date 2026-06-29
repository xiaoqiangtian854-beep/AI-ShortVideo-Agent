import unittest

from shortvideo_agent.planner import BriefValidationError, ContentBrief, build_content_plan


class PlannerTests(unittest.TestCase):
    def test_build_content_plan_creates_platform_specific_tasks(self):
        brief = ContentBrief(
            topic="AI tools for restaurant short videos",
            audience="small restaurant owners",
            platform="douyin",
            goal="drive private traffic leads",
            tone="practical and energetic",
            duration_seconds=45,
        )

        plan = build_content_plan(brief)

        self.assertEqual(plan.platform, "douyin")
        self.assertIn("3-second hook", plan.script_outline[0].lower())
        self.assertIn("comment prompt", " ".join(plan.publishing_notes).lower())
        self.assertGreaterEqual(len(plan.review_checks), 4)

    def test_build_content_plan_rejects_missing_required_fields(self):
        brief = ContentBrief(
            topic="",
            audience="creators",
            platform="wechat_channels",
            goal="increase saves",
            tone="clear",
            duration_seconds=60,
        )

        with self.assertRaisesRegex(BriefValidationError, "topic"):
            build_content_plan(brief)

    def test_build_content_plan_normalizes_unknown_platform(self):
        brief = ContentBrief(
            topic="Monthly product update",
            audience="existing customers",
            platform="internal_channel",
            goal="explain the update",
            tone="calm and direct",
            duration_seconds=75,
        )

        plan = build_content_plan(brief)

        self.assertEqual(plan.platform, "internal_channel")
        self.assertTrue(
            any("general short-video" in note.lower() for note in plan.publishing_notes)
        )


if __name__ == "__main__":
    unittest.main()
