from keras.models import model_from_json
import os
import tempfile
import numpy as np
from PIL import Image
from io import BytesIO
from .models import m_ClassField


model = None

def load_model():
    json_file = open('main/static/fmnist.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    global model
    model = model_from_json(loaded_model_json)
    model.load_weights("main/static/fmnist.h5")

def predict(file):

    global model
    if model is None:
        load_model()
    color_image = Image.open(file)
    image = np.array(color_image.convert("L").resize((28, 28)))
    pred_fit_image = image.reshape((1, 28, 28, 1))
    probs = model.predict(pred_fit_image)
    color_image = Image.open(file)
    height, width = color_image.size
    srow=int(height*.33)
    scol=int(width*.33)
    erow=int(height*.66)
    ecol=int(width*.66)
    crop = color_image.crop((srow,scol,erow,ecol))
    color_array = (crop.getcolors(maxcolors=999999))
    intended_color_count = color_array[0][0]
    intended_color = color_array[0][1]
    for _ in color_array:
        if _[0] > intended_color_count:
            intended_color_count = _[0]
            intended_color = _[1]

    prediction = m_ClassField.objects.get(id=np.argmax(probs))

    return {"prediction": prediction, "color":intended_color, "color_count":intended_color_count}
