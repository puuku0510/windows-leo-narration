"""Check that a purchased harness project is pinned to xAI's Leo voice.

This script reads configuration only. It does not import or modify the harness,
invoke an API, or create audio.
"""

import argparse
import json
import sys
from pathlib import Path


PRESET = "grok_leo"


def read_object(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object: {path}")
    return value


def check(work_dir: Path, harness_skill_dir: Path) -> None:
    narration = read_object(work_dir / "narration.json")
    if narration.get("voice") != PRESET:
        raise ValueError("narration.json must explicitly set voice to grok_leo")
    parts = narration.get("parts")
    slides = narration.get("slides")
    if not ((isinstance(parts, list) and parts) or (isinstance(slides, list) and slides)):
        raise ValueError("narration.json needs non-empty parts or slides")

    voices = read_object(harness_skill_dir / "data" / "voices.json")
    local_voices = work_dir / "voices.json"
    if local_voices.exists():
        voices.update(read_object(local_voices))
    selected = voices.get(PRESET)
    if not isinstance(selected, dict):
        raise ValueError("grok_leo preset is missing; add it using your licensed harness instructions")
    expected = {"provider": "xai", "voice_id": "leo", "language": "ja"}
    mismatches = [f"{key}={selected.get(key)!r}" for key, value in expected.items() if selected.get(key) != value]
    if mismatches:
        raise ValueError("grok_leo must resolve to xAI Leo in Japanese; found " + ", ".join(mismatches))
    print("OK: grok_leo -> provider=xai, voice_id=leo, language=ja")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("harness_skill_dir", type=Path)
    args = parser.parse_args()
    try:
        check(args.work_dir, args.harness_skill_dir)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Leo check failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
