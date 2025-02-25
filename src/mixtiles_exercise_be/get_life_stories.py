import random
import time
from functools import partial
from itertools import chain
from multiprocessing import Pool
from typing import List, Optional

import requests

from mixtiles_exercise_be.consts import (
    HUGGING_FACE_HEADERS,
    LLM_API_URL,
    NUM_LIFE_STORIES,
    NUM_SAMPLE_PHOTOS,
    PHOTO_ASSIGNMENT_BATCH_SIZE,
    PHOTO_ASSIGNMENT_NUM_PROCESSES,
)
from mixtiles_exercise_be.get_descriptions import get_photos_descriptions
from mixtiles_exercise_be.get_exif_data import get_photos_exif_data

full_photos_descriptions = []


def _generate_full_photos_descriptions(force_regenerate=False) -> List[str]:
    global full_photos_descriptions
    if not full_photos_descriptions or force_regenerate:
        photos_exif_data = get_photos_exif_data()
        photos_descriptions = get_photos_descriptions()
        full_photos_descriptions = [
            f"- {exif_data.date} - {exif_data.city} - {description}"
            for exif_data, description in zip(photos_exif_data, photos_descriptions)
        ]
    return full_photos_descriptions


def _generate_prompt_for_life_stories() -> str:
    full_descriptions = _generate_full_photos_descriptions()
    return f"""
### Instruction:
You are an AI that organizes photo descriptions into meaningful life stories.

### User:
I have random photos from a client's phone. I have a description, location, and timestamp for each photo.
Given those random photos, please generate {NUM_LIFE_STORIES} "Life Stories" that are found in the photos.
A "Life Story" is a sequence of events that are related to each other in a meaningful way.
"Life Story" examples: "Trip to Italy", "Hike in a mountain in Gleneagle".
Please provide a title for each "Life Story", and nothing more.

Those are the photo descriptions with timestamp and location:
{'\n'.join(random.sample(full_descriptions, NUM_SAMPLE_PHOTOS))}

### Assistant:
Here are {NUM_LIFE_STORIES} "Life Stories" titles found in the photos:
1."""


def _generate_prompt_for_photo_assignment_into_life_story(
    life_stories: List[str], some_full_photos_descriptions: List[str]
) -> str:
    return f"""
### Instruction:
You are an AI that assign photo descriptions (with date and location) into pre-defined categories.

### User:
Here are {NUM_LIFE_STORIES} "life stories" that were generated from the photos:
{'\n'.join(life_stories)}

For each photo (with date and location), assign it to one of those {NUM_LIFE_STORIES} "life story" (or "None").
Each "life story" can have multiple photos assigned to it, and MUST have at least one photo assigned to it.

{'\n'.join(some_full_photos_descriptions)}

### Assistant:
Here are assignment of each photo to a category (or "None"), by their order:
- 
"""


life_stories = []
life_stories_response = None


def get_life_stories(force_regenerate=False) -> List[str]:
    global life_stories, life_stories_response
    if not life_stories or force_regenerate:
        prompt_for_life_stories = _generate_prompt_for_life_stories()
        start_time = time.time()
        print(f"Gathering life stories (1 call to LLM API)...")
        response = requests.post(
            LLM_API_URL,
            headers=HUGGING_FACE_HEADERS,
            json={"inputs": prompt_for_life_stories, "parameters": {"max_new_tokens": 300}},
        )
        print("Time taken for life stories gathering:", time.time() - start_time)
        response.raise_for_status()
        life_stories_response = response.json()[0]["generated_text"]
        response_lines = life_stories_response.splitlines()
        life_stories_lines = response_lines[-NUM_LIFE_STORIES:]
        life_stories = [line[3:].replace('"', "") for line in life_stories_lines]
    return life_stories


photos_life_stories = []
photos_life_stories_response = None


def _extract_life_story(life_stories_line: str, life_stories: List[str]) -> Optional[str]:
    for life_story in life_stories:
        if life_story.lower() in life_stories_line.lower():
            return life_story
    return None


def _get_photos_life_stories_batch(
    life_stories: List[str], some_full_photos_descriptions: List[str]
) -> List[Optional[str]]:
    global photos_life_stories_response
    prompt_for_photo_assignment_into_life_story = _generate_prompt_for_photo_assignment_into_life_story(
        life_stories, some_full_photos_descriptions
    )
    start_time = time.time()
    response = requests.post(
        LLM_API_URL,
        headers=HUGGING_FACE_HEADERS,
        json={
            "inputs": prompt_for_photo_assignment_into_life_story,
            "parameters": {"max_new_tokens": 20 * len(some_full_photos_descriptions)},
        },
    )
    print(
        f"Time taken for photos assignment - 1 batch (of {len(some_full_photos_descriptions)} photos):",
        time.time() - start_time,
    )
    response.raise_for_status()
    num_photos = len(some_full_photos_descriptions)
    photos_life_stories_response = response.json()[0]["generated_text"]
    response_lines = photos_life_stories_response.splitlines()
    life_stories_lines = [line for line in response_lines if line.startswith("- ")][-num_photos:]
    some_photos_life_stories = [
        _extract_life_story(life_stories_line, life_stories) for life_stories_line in life_stories_lines
    ]
    return some_photos_life_stories


def get_photos_life_stories(force_regenerate=False) -> List[Optional[str]]:
    global photos_life_stories
    if not photos_life_stories or force_regenerate:
        life_stories = get_life_stories()
        full_photos_descriptions = _generate_full_photos_descriptions()
        full_photos_descriptions_batches = [
            full_photos_descriptions[i : i + PHOTO_ASSIGNMENT_BATCH_SIZE]
            for i in range(0, len(full_photos_descriptions), PHOTO_ASSIGNMENT_BATCH_SIZE)
        ]
        start_time = time.time()
        print(
            f"Assiging photos to life stories... ({len(full_photos_descriptions_batches)} calls - 1 per batch of {PHOTO_ASSIGNMENT_BATCH_SIZE} - to LLM API)"
        )
        with Pool(PHOTO_ASSIGNMENT_NUM_PROCESSES) as pool:
            photos_life_stories_lists = pool.map(
                partial(_get_photos_life_stories_batch, life_stories), full_photos_descriptions_batches
            )
        print(
            f"Time taken for photos assignment - total ({len(full_photos_descriptions_batches)} batches):",
            time.time() - start_time,
        )
        photos_life_stories = list(chain.from_iterable(photos_life_stories_lists))
    return photos_life_stories


photos_life_stories_filtered = []


def get_photos_life_stories_filtered(force_regenerate=False) -> List[Optional[str]]:
    global photos_life_stories_filtered
    if not photos_life_stories_filtered or force_regenerate:
        photos_life_stories = get_photos_life_stories()
        # TODO: Filter out some of the photos. How?
        # - Use a model to rank photo "quality".
        # - Filter out photos that were taken within seconds of each other.
        # - Use an LLM to choose the best photos based on their descriptions.
        photos_life_stories_filtered = photos_life_stories
    return photos_life_stories_filtered
