from nanonets import ImageClassification
import os, sys

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['damaged', 'not_damaged']

IMAGE_PATH = sys.argv[1]

model = ImageClassification(API_KEY, CATEGORIES, model_id=MODEL_ID)

result = model.predict_for_file(IMAGE_PATH)

print(result)