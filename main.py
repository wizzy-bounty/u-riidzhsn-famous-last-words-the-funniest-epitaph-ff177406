import os
from pathlib import Path

LINE = "I bet my life on 'probably.' I lost."


def write_entry():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main():
    write_entry()


if __name__ == "__main__":
    main()
