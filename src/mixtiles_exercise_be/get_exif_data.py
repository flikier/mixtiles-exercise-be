import time
from dataclasses import dataclass
from typing import List

import exifread
from geopy.geocoders import Nominatim

from mixtiles_exercise_be.consts import EXIF_NO_CITY_STR, EXIF_NO_DATE_STR
from mixtiles_exercise_be.get_photos import get_photos


@dataclass
class ExifData:
    date: str
    city: str


NO_EXIF_DATA = ExifData(date=EXIF_NO_DATE_STR, city=EXIF_NO_CITY_STR)


def _get_exif_data(image_path):
    """Extracts EXIF metadata from the image."""
    with open(image_path, "rb") as f:
        tags = exifread.process_file(f)

    exif_data = {
        "datetime": tags.get("EXIF DateTimeOriginal"),
        "latitude": None,
        "longitude": None,
        "latitude_ref": None,
        "longitude_ref": None,
    }

    if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
        exif_data["latitude"] = tags["GPS GPSLatitude"]
        exif_data["longitude"] = tags["GPS GPSLongitude"]
        exif_data["latitude_ref"] = tags["GPS GPSLatitudeRef"].values[0]
        exif_data["longitude_ref"] = tags["GPS GPSLongitudeRef"].values[0]

    return exif_data


def _convert_to_degrees(value):
    """Converts GPS coordinates from EXIF format to decimal degrees."""
    d, m, s = value.values
    return float(d.num) / float(d.den) + float(m.num) / (float(m.den) * 60) + float(s.num) / (float(s.den) * 3600)


def get_city_from_coordinates(lat, lon):
    """Uses reverse geocoding to get the city from GPS coordinates."""
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.reverse((lat, lon), exactly_one=True)

    if location:
        return location.raw.get("address", {}).get("city", EXIF_NO_CITY_STR)
    return EXIF_NO_CITY_STR


def get_image_info(image_path) -> ExifData:
    """Extracts both the date and city from the image EXIF metadata."""
    exif_data = _get_exif_data(image_path)

    # Extract date
    date_taken = exif_data["datetime"]
    date_taken = str(date_taken) if date_taken else EXIF_NO_DATE_STR

    # Extract city
    city = EXIF_NO_CITY_STR
    if exif_data["latitude"] and exif_data["longitude"]:
        lat = _convert_to_degrees(exif_data["latitude"])
        lon = _convert_to_degrees(exif_data["longitude"])

        # Handle hemisphere (N/S, E/W)
        if exif_data["latitude_ref"] != "N":
            lat = -lat
        if exif_data["longitude_ref"] != "E":
            lon = -lon

        city = get_city_from_coordinates(lat, lon)

    return ExifData(date=date_taken, city=city)


photos_exif_data = []


def get_photos_exif_data(force_regenerate=False) -> List[ExifData]:
    global photos_exif_data
    photos = get_photos()
    if not photos_exif_data or force_regenerate:
        start_time = time.time()
        print("Extracting EXIF data from photos...")
        photos_exif_data = [get_image_info(photo) for photo in photos]
        print(f"Time taken for extracting EXIF data: {time.time() - start_time:.2f} seconds.")
    return photos_exif_data


if __name__ == "__main__":
    print(get_photos_exif_data())
