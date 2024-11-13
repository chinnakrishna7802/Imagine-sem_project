import matplotlib.pyplot as plt
import cv2
from tensorflow import keras
import IE.Functionalmodel as Fm
from IE.SubpixelConv2D import SubpixelConv2D
import numpy as np
from PIL import Image
from IE.utils import get_data,loadimg



def prediction_enhan(img):
    input_image = get_data(img)
    

    G = Fm.get_G((96, 96, 3))
    model = 5000
    G = keras.models.load_model(f'IE/results/gener_{model}_h5', custom_objects = {'SubpixelConv2D' : SubpixelConv2D},compile=False)
    output_image = G.predict(input_image)
    print(type(output_image))
    output_image= Image.fromarray(np.uint8(output_image.squeeze()*255))
    output_image = np.asarray(output_image)

    input_image = np.array(input_image.squeeze()*255, dtype=np.uint8)
    return output_image, input_image
    
