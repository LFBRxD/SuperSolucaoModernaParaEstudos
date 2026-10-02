# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import academia_hub
import academia_w01_04
import academia_w05_08
import academia_w09_12

if __name__ == "__main__":
    academia_hub.build()
    academia_w01_04.build()
    academia_w05_08.build()
    academia_w09_12.build()
    root = Path(__file__).resolve().parents[1] / "docs" / "academia-qa"
    n = len(list(root.rglob("*.md")))
    print(f"MARKDOWN_COUNT={n}")
