import io
import time
from multiprocessing import Pool
from typing import List, Tuple

import requests
from PIL import Image

from mixtiles_exercise_be.consts import (
    HUGGING_FACE_HEADERS,
    IMAGE_CAPTION_API_URL,
    IMAGE_CAPTION_ERROR_STR,
    IMAGE_CAPTION_NUM_PROCESSES,
    IMAGE_CAPTION_NUM_RETRY,
    IMAGE_CAPTION_RESIZE,
)
from mixtiles_exercise_be.get_photos import get_photos


def resize_photo_to_memory(photo_path: str, max_size: Tuple[float, float]) -> io.BytesIO:
    img = Image.open(photo_path)
    img.thumbnail(max_size)  # Resize while preserving aspect ratio
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")  # Save to memory as JPEG (change format if needed)
    img_bytes.seek(0)  # Move to the start of the stream
    return img_bytes  # This behaves like open(photo_path, "rb")


def get_photo_caption(photo_buffer: io.BytesIO) -> str:
    response = requests.post(IMAGE_CAPTION_API_URL, headers=HUGGING_FACE_HEADERS, data=photo_buffer.read())
    result = response.json()[0]["generated_text"]
    return result


def get_photo_description(photo_path: str) -> str:
    for _ in range(IMAGE_CAPTION_NUM_RETRY):
        try:
            result = get_photo_caption(resize_photo_to_memory(photo_path, IMAGE_CAPTION_RESIZE))
            return result
        except Exception:
            pass
    print(f"Failed to get photo description for {photo_path} after {IMAGE_CAPTION_NUM_RETRY} retries.")
    return IMAGE_CAPTION_ERROR_STR


photos_descriptions = []


def get_photos_descriptions(force_regenerate=False) -> List[str]:
    global photos_descriptions
    if not photos_descriptions or force_regenerate:
        start_time = time.time()
        print("Getting photo descriptions...")
        with Pool(IMAGE_CAPTION_NUM_PROCESSES) as pool:
            photos_descriptions = pool.map(get_photo_description, get_photos())
        print(f"Time taken for getting photo descriptions: {time.time() - start_time:.2f} seconds.")
    return photos_descriptions


if __name__ == "__main__":
    print(get_photos_descriptions())
