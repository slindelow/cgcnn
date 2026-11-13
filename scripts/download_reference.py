"""Restore the pinned CaMML teaching materials into the ignored reference folder."""
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "docs/reference-manifest.json").read_text())
destination = root / "reference/camml"
destination.mkdir(parents=True, exist_ok=True)
for entry in manifest["files"]:
    path = destination / entry["name"]
    if path.exists():
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"Local reference changed; preserve it before restoring: {path}")
        print(f"Verified {entry['name']}")
        continue
    with urlopen(entry["url"], timeout=60) as response:
        content = response.read()
    if hashlib.sha256(content).hexdigest() != entry["sha256"]:
        raise RuntimeError(f"Checksum mismatch: {entry['name']}")
    path.write_bytes(content)
    print(f"Downloaded {entry['name']}")
