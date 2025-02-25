
# Mixtiles Exercise - BE


## How to generate life stories of photos

1. Make sure [photos.json](data/photos.json) includes the photos you want to generate life stories for.

1. Make sure to update those 2 values in [consts.py](src/mixtiles_exercise_be/consts.py):

   ```python
   # HUGGING_FACE_TOKEN: Get a token here: https://huggingface.co/settings/tokens
   # HUGGING_FACE_TOKEN - Example: "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
   HUGGING_FACE_TOKEN = "XXX"
   
   # LLM_API_URL: Run `mistralai/Mistral-7B-Instruct-v0.3` on `Nvidia T4 16 GB` here: https://endpoints.huggingface.co
   # LLM_API_URL - Example: "https://cw2ku8v0okq8iggq.us-east-1.aws.endpoints.huggingface.cloud"
   LLM_API_URL = "XXX"
   ```

1. Run the following commands:

   ```shell
   poetry install
   poetry run python src/mixtiles_exercise_be/generate_photos_life_stories.py
   ```

1. Copy the generated file [lifeStories.json](data/) to the [UI data directory](https://github.com/flikier/mixtiles-exercise-fe/tree/main/src/data).

1. Make sure all photos are available in the [UI photos directory](https://github.com/flikier/mixtiles-exercise-fe/tree/main/public/photos).

## Example output

### With MAX_PHOTOS_TO_PROCESS = 200

- File output: [See here](data/lifeStories_MAX_PHOTOS_TO_PROCESS_200.json)

- Shell output:

  ```shell
  --> Generating photos life stories...
  --vvv-- (1) Loading photos...
  Loading photos...
  --^^^-- (1) Loaded 200 photos.
  --vvv-- (2) Getting photos exif data...
  Extracting EXIF data from photos...
  Time taken for extracting EXIF data: 164.70 seconds.
  --^^^-- (2) Got 199 photos exif data.
  --vvv-- (3) Generating photos descriptions...
  Getting photo descriptions...
  Failed to get photo description for /home/itay/Downloads/photos/Photos/
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0206.JPEG after 3 retries.
  Time taken for getting photo descriptions: 165.96 seconds.
  --^^^-- (3) Generated 198 photos descriptions.
  --vvv-- (4) Generating life stories...
  Gathering life stories (1 call to LLM API)...
  Time taken for life stories gathering: 6.444242477416992
  --^^^-- (4) Generated 5 life stories: Adventure in Colorado Springs, Exploring Caves, Family Time in Gleneagle, A Day at the Zoo, Traveling Unknown Cities
  --vvv-- (5) Assigning photos to life stories...
  Assiging photos to life stories... (7 calls - 1 per batch of 30 - to LLM API)
  Time taken for photos assignment - 1 batch (of 20 photos): 28.694435358047485
  Time taken for photos assignment - 1 batch (of 30 photos): 41.87624931335449
  Time taken for photos assignment - 1 batch (of 30 photos): 41.95106649398804
  Time taken for photos assignment - 1 batch (of 30 photos): 41.95282244682312
  Time taken for photos assignment - 1 batch (of 30 photos): 41.95252323150635
  Time taken for photos assignment - 1 batch (of 30 photos): 41.958805322647095
  Time taken for photos assignment - 1 batch (of 30 photos): 41.958528995513916
  Time taken for photos assignment - total (7 batches): 41.998810052871704
  --^^^-- (5) Assigned 107 photos to life stories. Value counts per life story: Adventure in Colorado Springs: 42, Exploring Caves: 13, Family Time in Gleneagle: 44, A Day at the Zoo: 5, Traveling Unknown Cities: 3
  --vvv-- (6) Filtering photos life stories...
  --^^^-- (6) Filtered 107 photos life stories. Value counts per life story: Adventure in Colorado Springs: 42, Exploring Caves: 13, Family Time in Gleneagle: 44, A Day at the Zoo: 5, Traveling Unknown Cities: 3
  --> Saving photos life stories...
  --> Photos life stories saved successfully to output file: data/lifeStories.json
  ```

### With MAX_PHOTOS_TO_PROCESS = 1000

- File output: [See here](data/lifeStories_MAX_PHOTOS_TO_PROCESS_1000.json)

- Shell output:

  ```shell
  --> Generating photos life stories...
  --vvv-- (1) Loading photos...
  Loading photos...
  --^^^-- (1) Loaded 923 photos.
  --vvv-- (2) Getting photos exif data...
  Extracting EXIF data from photos...
  Time taken for extracting EXIF data: 879.97 seconds.
  --^^^-- (2) Got 922 photos exif data.
  --vvv-- (3) Generating photos descriptions...
  Getting photo descriptions...
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0206.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0150.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0407.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0349.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0336.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0439.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0475.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0249.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0488.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0476.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0429.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0452.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0250.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0265.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0489.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0541.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0350.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0266.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0253.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0430.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0297-1.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0477.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0453.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0440.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0409.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0351.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0337.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0257.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0575.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0542.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0462.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0305.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0585.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0512.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0267.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0431.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0283.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0490.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0533.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0322.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0478.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0298.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0411.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0454.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0339.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0463.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0441.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0257.JPG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0587.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0352.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_0640.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_1212.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_1077.JPEG after 3 retries.
  Failed to get photo description for /home/itay/Downloads/photos/Photos/IMG_1256.JPEG after 3 retries.
  Time taken for getting photo descriptions: 489.39 seconds.
  --^^^-- (3) Generated 869 photos descriptions.
  --vvv-- (4) Generating life stories...
  Gathering life stories (1 call to LLM API)...
  Time taken for life stories gathering: 7.095196723937988
  --^^^-- (4) Generated 5 life stories: Snowy Days in Gleneagle, Exploring Colorado Springs, Cooking and Baking in the Kitchen, A Trip to the Zoo, A Day at the Concert in Oakland
  --vvv-- (5) Assigning photos to life stories...
  Assiging photos to life stories... (31 calls - 1 per batch of 30 - to LLM API)
  Time taken for photos assignment - 1 batch (of 30 photos): 53.99769568443298
  Time taken for photos assignment - 1 batch (of 30 photos): 55.02873706817627
  Time taken for photos assignment - 1 batch (of 30 photos): 55.11843276023865
  Time taken for photos assignment - 1 batch (of 30 photos): 55.122599363327026
  Time taken for photos assignment - 1 batch (of 30 photos): 55.12350654602051
  Time taken for photos assignment - 1 batch (of 30 photos): 55.12437200546265
  Time taken for photos assignment - 1 batch (of 30 photos): 55.127246379852295
  Time taken for photos assignment - 1 batch (of 30 photos): 55.26032376289368
  Time taken for photos assignment - 1 batch (of 30 photos): 56.09260010719299
  Time taken for photos assignment - 1 batch (of 30 photos): 56.18432307243347
  Time taken for photos assignment - 1 batch (of 30 photos): 56.18519687652588
  Time taken for photos assignment - 1 batch (of 30 photos): 56.18544125556946
  Time taken for photos assignment - 1 batch (of 30 photos): 56.186511754989624
  Time taken for photos assignment - 1 batch (of 30 photos): 56.187196016311646
  Time taken for photos assignment - 1 batch (of 30 photos): 58.50151586532593
  Time taken for photos assignment - 1 batch (of 30 photos): 58.57330656051636
  Time taken for photos assignment - 1 batch (of 30 photos): 58.57408165931702
  Time taken for photos assignment - 1 batch (of 23 photos): 35.695533752441406
  Time taken for photos assignment - 1 batch (of 30 photos): 101.09009861946106
  Time taken for photos assignment - 1 batch (of 30 photos): 101.67075562477112
  Time taken for photos assignment - 1 batch (of 30 photos): 47.67155170440674
  Time taken for photos assignment - 1 batch (of 30 photos): 101.68008661270142
  Time taken for photos assignment - 1 batch (of 30 photos): 46.56196904182434
  Time taken for photos assignment - 1 batch (of 30 photos): 46.70472860336304
  Time taken for photos assignment - 1 batch (of 30 photos): 46.78898000717163
  Time taken for photos assignment - 1 batch (of 30 photos): 46.70449209213257
  Time taken for photos assignment - 1 batch (of 30 photos): 46.711220026016235
  Time taken for photos assignment - 1 batch (of 30 photos): 46.70846176147461
  Time taken for photos assignment - 1 batch (of 30 photos): 45.76594042778015
  Time taken for photos assignment - 1 batch (of 30 photos): 45.85736083984375
  Time taken for photos assignment - 1 batch (of 30 photos): 46.86688208580017
  Time taken for photos assignment - total (31 batches): 102.06284379959106
  --^^^-- (5) Assigned 310 photos to life stories. Value counts per life story: Snowy Days in Gleneagle: 89, Exploring Colorado Springs: 70, Cooking and Baking in the Kitchen: 111, A Trip to the Zoo: 19, A Day at the Concert in Oakland: 21
  --vvv-- (6) Filtering photos life stories...
  --^^^-- (6) Filtered 310 photos life stories. Value counts per life story: Snowy Days in Gleneagle: 89, Exploring Colorado Springs: 70, Cooking and Baking in the Kitchen: 111, A Trip to the Zoo: 19, A Day at the Concert in Oakland: 21
  --> Saving photos life stories...
  --> Photos life stories saved successfully to output file: data/lifeStories.json
  ```
