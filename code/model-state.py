import os
import json
from nanonets import ImageClassification

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['damaged', 'not_damaged']

model = ImageClassification(API_KEY, CATEGORIES, model_id=MODEL_ID)

response = model._check_model_state()

if response["state"] == 5:
	print("NEXT RUN: python ./code/prediction.py ./images/damaged-40.jpg")