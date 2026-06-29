# Contributing

Thanks for your interest in AI ShortVideo Agent.

## Good First Contributions

- Add a new platform workflow in `docs/workflows/`.
- Improve a prompt template in `prompts/`.
- Add an anonymized example brief in `examples/`.
- Add tests for `src/shortvideo_agent/planner.py`.

## Contribution Flow

1. Open an issue describing the workflow, prompt, or code change.
2. Keep examples practical and anonymized.
3. Run the test suite before opening a pull request:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

4. In the pull request, explain the target user and platform.

## Content Guidelines

- Do not include private customer data, credentials, or unreleased business plans.
- Use original text and examples.
- If a prompt depends on a platform rule, link to the official source when possible.
- Prefer repeatable workflows over one-off growth hacks.

