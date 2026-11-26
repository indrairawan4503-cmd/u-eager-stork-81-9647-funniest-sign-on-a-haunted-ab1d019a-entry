"""Haunted server room sign entry (variant A): the ghost with the password.

Writes exactly one funny line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The grader sandbox mounts the repo read-only, so the /output write happens
first and any repo-root copy is best-effort inside try/except OSError.

The line is the v8 iteration of one concept: a warning sign telling staff
not to reboot the ghost, because he holds the only admin password and died
mid-ticket. "Has" beat "holds" for punch; the comma keeps the two-beat
rhythm before the kicker.
"""

import os

MAX_CHARS = 120

ENTRY_TEXT = (
    "DO NOT REBOOT THE GHOST. He has the only admin password, "
    "and he died mid-ticket."
)


def check_entry_text() -> None:
    if not (1 <= len(ENTRY_TEXT) <= MAX_CHARS):
        raise ValueError(
            f"ENTRY_TEXT must be 1..{MAX_CHARS} chars, got {len(ENTRY_TEXT)}"
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("ENTRY_TEXT must not be only whitespace")


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> None:
    check_entry_text()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def copy_to_repo_root() -> None:
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(repo_root, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    check_entry_text()
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
