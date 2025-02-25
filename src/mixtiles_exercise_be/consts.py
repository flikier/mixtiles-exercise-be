###
# General
###

MAX_PHOTOS_TO_PROCESS = 1000
INPUT_FILENAME = "data/photos.json"
OUTPUT_FILENAME = "data/lifeStories.json"
# HUGGING_FACE_TOKEN: Get a token here: https://huggingface.co/settings/tokens
# HUGGING_FACE_TOKEN - Example: "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
HUGGING_FACE_TOKEN = "XXX"
HUGGING_FACE_HEADERS = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}


###
# Photo Exif Data Extraction
###

EXIF_NO_DATE_STR = "No date found"
EXIF_NO_CITY_STR = "No city found"


###
# Photo Description Generation
###

IMAGE_CAPTION_NUM_RETRY = 3
# 256x256 found empirically to be good enough for relevant description.
IMAGE_CAPTION_RESIZE = (256, 256)
IMAGE_CAPTION_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
IMAGE_CAPTION_NUM_PROCESSES = 20
IMAGE_CAPTION_ERROR_STR = "No photo description available"

###
# Life Stories Generation
###

NUM_LIFE_STORIES = 5
NUM_SAMPLE_PHOTOS = 200
# LLM_API_URL: Run `mistralai/Mistral-7B-Instruct-v0.3` on `Nvidia T4 16 GB` here: https://endpoints.huggingface.co
# LLM_API_URL - Example: "https://cw2ku8v0okq8iggq.us-east-1.aws.endpoints.huggingface.cloud"
LLM_API_URL = "XXX"


###
# Photo Assignment
###

PHOTO_ASSIGNMENT_BATCH_SIZE = 30
PHOTO_ASSIGNMENT_NUM_PROCESSES = 20


###
# Check Constants
###

assert HUGGING_FACE_TOKEN != "XXX", "Please set your Hugging Face token (HUGGING_FACE_TOKEN) in consts.py"
assert LLM_API_URL != "XXX", "Please set your LLM API URL (LLM_API_URL) in consts.py"
