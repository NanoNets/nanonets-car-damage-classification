import os
from nanonets import ImageClassification

API_KEY = os.environ.get('NANONETS_API_KEY')
CATEGORIES = ['damaged', 'not_damaged']

IMAGE_DIR = './images/'

model = ImageClassification(API_KEY, CATEGORIES)

images = [IMAGE_DIR + x for x in os.listdir(IMAGE_DIR)]
images.sort()

annotations = [x.split('/')[-1].split('-')[0] for x in images]
annotations.sort()

training_dict = dict(zip(images, annotations))

response = model.train(training_dict)

print("NEXT RUN: export NANONETS_MODEL_ID=" + model.model_id)
print("NEXT RUN: python ./code/model-state.py")
