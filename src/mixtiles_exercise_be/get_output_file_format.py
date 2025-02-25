import json
from pathlib import Path
from typing import Dict

from mixtiles_exercise_be.consts import OUTPUT_FILENAME
from mixtiles_exercise_be.get_descriptions import get_photos_descriptions
from mixtiles_exercise_be.get_life_stories import get_life_stories, get_photos_life_stories_filtered
from mixtiles_exercise_be.get_photos import get_photos


def get_output_file_data() -> Dict:
    photos = get_photos()
    photos_descriptions = get_photos_descriptions()
    life_stories = get_life_stories()
    photos_life_stories_filtered = get_photos_life_stories_filtered()
    life_story_to_photos = {
        life_story: [
            photo
            for photo, photo_life_story in zip(photos, photos_life_stories_filtered)
            if photo_life_story == life_story
        ]
        for life_story in life_stories
    }
    photo_to_description = {photo: description for photo, description in zip(photos, photos_descriptions)}
    return {
        "photoGroups": [
            {
                "id": str(life_story_id),
                "title": life_story,
                "photos": [
                    {
                        "id": f"{life_story_id}-{photo_id}",
                        "url": f"/public/photos/{Path(photo).name}",
                        "title": photo_to_description[photo],
                    }
                    for photo_id, photo in enumerate(life_story_to_photos[life_story])
                ],
            }
            for life_story_id, life_story in enumerate(life_stories)
        ]
    }


def save_output_file_data() -> None:
    output_file_data = get_output_file_data()
    with open(Path(__file__).parent.parent.parent / OUTPUT_FILENAME, "w") as f:
        json.dump(output_file_data, f, indent=2)
