import json
from pathlib import Path
from typing import List

from mixtiles_exercise_be.consts import INPUT_FILENAME, MAX_PHOTOS_TO_PROCESS

photos = []


def get_photos(force_regenerate=False) -> List[str]:
    global photos
    if not photos or force_regenerate:
        print("Loading photos...")
        with open(Path(__file__).parent.parent.parent / INPUT_FILENAME, "r") as f:
            photos = json.load(f)[:MAX_PHOTOS_TO_PROCESS]
    return photos
