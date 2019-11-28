<div align="center">
  <a href="https://nanonets.com/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets Car Damage Inspection" width="100"/>
    </a>
</div>

<h1 align="center">NanoNets Car Damage Inspection</h1>

** **

## Car Damage Classification with Nanonets

A simple classifier used to classify images of damaged cars from non-damaged cars using the Nanonets API. You can find the example to train a model in python, by updating the api-key and model id in corresponding file.

** **

# Build a Car Damage Classification Model

>**Note:** Make sure you have python and pip installed on your system if you don't visit
[Python](https://www.python.org/downloads/release/python-2714/), 
[pip](https://pip.pypa.io/en/stable/installing/)


### Step 1: Clone the Repo, Install dependencies
```bash
git clone https://github.com/NanoNets/nanonets-car-damage-classification.git
cd nanonets-car-damage-classification
sudo pip install nanonets
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/#/keys

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Upload Images For Training
The training data is found in ```images``` 
```bash
python ./code/training.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model-state.py
```

### Step 7: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./images/damaged-40.jpg
```


*Note the python sample uses the converted json instead of the xml payload for convenience purposes, hence it has no dependencies.*
