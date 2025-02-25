from mixtiles_exercise_be.consts import IMAGE_CAPTION_ERROR_STR, OUTPUT_FILENAME
from mixtiles_exercise_be.get_descriptions import get_photos_descriptions
from mixtiles_exercise_be.get_exif_data import NO_EXIF_DATA, get_photos_exif_data
from mixtiles_exercise_be.get_life_stories import (
    get_life_stories,
    get_photos_life_stories,
    get_photos_life_stories_filtered,
)
from mixtiles_exercise_be.get_output_file_format import save_output_file_data
from mixtiles_exercise_be.get_photos import get_photos


def generate_photos_life_stories():
    print("--> Generating photos life stories...")

    print(f"--vvv-- (1) Loading photos...")
    photos = get_photos()
    print(f"--^^^-- (1) Loaded {len(photos)} photos.")

    print(f"--vvv-- (2) Getting photos exif data...")
    photos_exif_data = get_photos_exif_data()
    print(f"--^^^-- (2) Got {len([ped for ped in photos_exif_data if ped != NO_EXIF_DATA])} photos exif data.")

    print(f"--vvv-- (3) Generating photos descriptions...")
    photos_descriptions = get_photos_descriptions()
    print(
        f"--^^^-- (3) Generated {len([pd for pd in photos_descriptions if pd != IMAGE_CAPTION_ERROR_STR])} photos descriptions."
    )

    print(f"--vvv-- (4) Generating life stories...")
    life_stories = get_life_stories()
    print(f"--^^^-- (4) Generated {len(life_stories)} life stories: {', '.join(life_stories)}")

    print(f"--vvv-- (5) Assigning photos to life stories...")
    photos_life_stories = get_photos_life_stories()
    print(
        f"--^^^-- (5) Assigned {len([pls for pls in photos_life_stories if pls is not None])} photos to life stories. "
        + f"Value counts per life story: {', '.join([f'{life_story}: {photos_life_stories.count(life_story)}' for life_story in life_stories])}"
    )

    print("--vvv-- (6) Filtering photos life stories...")
    photos_life_stories_filtered = get_photos_life_stories_filtered()
    print(
        f"--^^^-- (6) Filtered {len([plsf for plsf in photos_life_stories_filtered if plsf is not None])} photos life stories. "
        + f"Value counts per life story: {', '.join([f'{life_story}: {photos_life_stories_filtered.count(life_story)}' for life_story in life_stories])}"
    )

    print("--> Saving photos life stories...")
    save_output_file_data()
    print("--> Photos life stories saved successfully to output file:", OUTPUT_FILENAME)


if __name__ == "__main__":
    generate_photos_life_stories()
